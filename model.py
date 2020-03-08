import torch
import torch.nn as nn


class Encoder(nn.Module):
    def __init__(self, graphemes_size, hidden_size):
        super(Encoder, self).__init__()
        self.graphemes_size = graphemes_size
        self.hidden_size = hidden_size

        self.emb = nn.Embedding(graphemes_size, hidden_size)
        self.rnn = nn.GRU(hidden_size, hidden_size, bidirectional=True)

    def forward(self, x):
        # x: TxN
        T, N = x.size()
        emb = self.emb(x)  # emb: TxNxH
        output, _ = self.rnn(emb)  # output: TxNxH, hidden: 1XNxH
        output = output.view(T, N, 2, -1).sum(2)  # reduce bi-RNN by sum
        return output


class Decoder(nn.Module):
    def __init__(self, phonemes_size, hidden_size):
        super(Decoder, self).__init__()
        self.phonemes_size = phonemes_size
        self.hidden_size = hidden_size

        self.emb = nn.Embedding(phonemes_size, hidden_size)
        self.attn_combine = nn.Linear(2 * hidden_size, hidden_size)
        self.rnn = nn.GRU(hidden_size, hidden_size)
        self.fc = nn.Linear(hidden_size, phonemes_size, bias=False)

    def forward(self, x, enc, hidden):
        # x: 1xN, enc: T(enc)xNxH, hidden: 1xNxH
        emb = self.emb(x)  # emb: 1xNxH

        shaped_hidden = hidden.squeeze(0).unsqueeze(2).contiguous()
        shaped_act_hidden = torch.tanh(shaped_hidden)
        shaped_enc = enc.transpose(0, 1).contiguous()
        shaped_act_enc = torch.tanh(shaped_enc)
        e = torch.bmm(shaped_act_enc, shaped_act_hidden)  # NxT(enc)x1
        att_weights = torch.softmax(e, 1).squeeze(2).unsqueeze(1)
        att_vec = torch.bmm(att_weights, shaped_enc)
        att_vec = att_vec.transpose(1, 0).contiguous()

        x = torch.cat([att_vec, emb], dim=2)
        x = self.attn_combine(x)

        output, hidden = self.rnn(x, hidden)  # output: 1xNxH, hidden: 1XNxH

        T, N, H = output.size()
        output = output.view(T * N, H)
        output = self.fc(output)
        output = output.view(T, N, self.phonemes_size)

        return output, hidden, att_weights


if __name__ == '__main__':
    encoder = Encoder(32, 128)
    decoder = Decoder(20, 128)

    x = torch.LongTensor([[0, 0], [3, 8], [4, 4], [3, 1], [1, 1]])
    enc = encoder(x)

    # decode for 2 time steps
    print('step 0')
    x0 = torch.LongTensor([[0, 0]])
    y0, hidden, att_weights0 = decoder(x0, enc)
    print('\n' * 3)
    print('step 1')
    # select x1 from y
    x1 = torch.LongTensor([[7, 4]])
    y1, hidden, att_weights1 = decoder(x1, enc, hidden)
