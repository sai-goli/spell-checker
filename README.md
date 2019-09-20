# spelling-corrector
a simple spell corrector based on Bayseian Probability implemented in Python
inspired from Norvig's Spell Corrector 
Idea:
  -given a word: w   
  -an mistake may be resulted from one of the operation: deletion, insertion, swapping, substitution
  -find all possible words with in one change from given word : e1
  -find all possible words within two changes from given word : e2
  -get set of all words by union of above sets : U = union(e1,e2)  
  -given a language model containing valid words and their probability of occurrence : lang
  -find all words in U which are valid: known_words = intersection(u,lang)
  -result the known word with highest probability in lang : max(known_words, key=probability)
