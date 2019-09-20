<h1> spell checker </h1> <br>

<strong>a simple spell corrector based on Bayseian Probability implemented in Python inspired from Norvig's Spell Corrector </strong><br>

<h3>Idea:</h3>   
  <ul>
  <li>given a word: w   </li>
  <li>an mistake may be resulted from one of the operation: deletion, insertion, swapping, substitution</li>   
  <li>find all possible words with in one change from given word : e1   </li>
  <li>find all possible words within two changes from given word : e2   </li>
  <li>get set of all words by union of above sets : U = union(e1,e2)     </li>
  <li>given a language model containing valid words and their probability of occurrence : lang   </li>
  <li>find all words in U which are valid: known_words = intersection(u,lang) </li>  
  <li>result the known word with highest probability in lang : max(known_words, key=probability)   </li>
</ul>
