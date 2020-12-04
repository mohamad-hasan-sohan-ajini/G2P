## Supported Languages
Currently the following languages are supported:
1. EN: Based on [The CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict).
2. FA: Based on [Zaya Dictionary](https://www.peykaregan.ir/dataset/%D9%88%D8%A7%DA%98%DA%AF%D8%A7%D9%86-%D8%B2%D8%A7%DB%8C%D8%A7%DB%8C-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C).
3. RU: Based on [vosk-model-ru-0.10](https://alphacephei.com/vosk/models)


## Contribution
You can clean and prune your language specific pronunciation dictionary and put it in the same structure as existing languages.<br>
Each language folder must contain the following json files:
1. ```Grapheme.json```: List of all graphemes used in dictionary.
2. ```Phonemes.json```: List of all phonemes used in dictionary.
3. ```Lexicon.json```: List of (word, pronunciation) tuples. Words with multiple pronunciations could be appeared as the first element of multiple tuples. For example the word "DIFFERENT" has two different pronunciatins, so it has 2 different entreis as follows:
```
[
    ...,
    ("DIFFERENT", "D IH F ER AH N T"),
    ("DIFFERENT", "D IH F R AH N T"),
    ...
]
```
