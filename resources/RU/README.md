# VOSK
[vosk](https://alphacephei.com/vosk/models)  vosk-model-ru-0.10.zip is a free russian model constists lexicon dictionary.
The corpus consist of 720k unique tockens.


## Preprocessing
The preprocessing stage consist of the following steps:
1. Find unique and frequent graphemes and phonemes.
2. Create json format dictionary while retaining all pronunciations of words.
3. Adding start of sequence (```<sos>```) and end of sequence (```<eos>```) tokens.



