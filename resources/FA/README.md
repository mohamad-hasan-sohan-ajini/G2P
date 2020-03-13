# Zaya Lexicon
[Zaya](https://www.peykaregan.ir/dataset/%D9%88%D8%A7%DA%98%DA%AF%D8%A7%D9%86-%D8%B2%D8%A7%DB%8C%D8%A7%DB%8C-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C) is a free persian lexicon distilled from a 10M token corpus.
The corpus consist of 100k unique tockens.
Elimination of morphological words yields a 44k entry lexicon.
Adding persian contemporary dictionary entries, it reaches to 55k word lexicon.



## Preprocessing
The preprocessing stage consist of the following steps:
1. Replace arabic chars with relevant persian chars (using [hazm](https://github.com/sobhe/hazm))
2. Find unique and frequent graphemes and phonemes.
3. Eliminate entries contain rare graphemes and phonems.
4. Create json format dictionary while retaining all pronunciations of words.
5. Adding start of sequence (```<sos>```) and end of sequence (```<eos>```) tokens.



## TODO
Legend of phonemes.
