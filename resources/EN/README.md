# The CMU Pronouncing Dictionary
[The CMU pronouncing dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict) is a free english lexicon.
The pronunciations are with respect to north american english and the dictionary contains over 134k words.



## Preprocessing
The preprocessing stage consist of the following steps:
1. Remove stress annotations.
2. Find unique and frequent graphemes and phonemes.
3. Eliminate entries contain rare graphemes and phonems (like numbers and punctuations).
4. Create json format dictionary while retaining all pronunciations of words.
5. Adding start of sequence (```<sos>```) and end of sequence tokens (```<eos>```).



## TODO
Legend of phonemes.
