import json

import torch

cpu = torch.device('cpu')
gpu = torch.device('cuda')


class DataConfig(object):
    graphemes_path = 'resources/Graphemes.json'
    phonemes_path = 'resources/Phonemes.json'
    lexicon_path = 'resources/Lexicon.json'


class ModelConfig(object):
    with open(DataConfig.graphemes_path) as f:
        graphemes_size = len(json.load(f))

    with open(DataConfig.phonemes_path) as f:
        phonemes_size = len(json.load(f))

    hidden_size = 128


class TrainConfig(object):
    device = gpu if torch.cuda.is_available() else cpu
    lr = 3e-4
    batch_size = 128
    epochs = 10
    log_path = 'log'


class TestConfig(object):
    device = cpu
    encoder_model_path = 'models/encoder_e10.pth'
    decoder_model_path = 'models/decoder_e10.pth'
