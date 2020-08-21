
import string
import re
from collections import Counter
# All english alphabets, a-z
LETTERS = string.ascii_lowercase

# function to get all possible words within one distance of change 
def edits1(word): # returns the list
	n = len(word)
	#words formed by deleting a letter, total n-ways
	del_ = [word[:i]+word[i+1:]  for i in range(len(word))]
	# words formed by inserting a letter, 26*(n+1)ways
	ins_ = [word[:i]+letter+word[i:] for i in range(len(word)+1) for letter in LETTERS] 
	#words formed by substituting with a letter, 26*n ways
	sub_ = [word[:i]+letter+word[i+1:] for i in range(len(word)) for letter in LETTERS]
	# words formed by swapping adjacent letters, n-1ways
	swap_ = [word[:i]+word[i+1]+word[i]+word[i+2:] for i in range(len(word)-1)] 
	# set of all possible letters
	all_edits = set(del_+ins_+sub_+swap_)
	return all_edits
	
def edits2(word): #returns set of all possible words within two edit changes
	return set( w2 for w1 in edits1(word) for w2 in edits1(w1))

#a text file containing more than one million English words
eng_file = open('big.txt').read()

# function to convert textto list of words
def words(text):
	return re.findall(r'\w+',text.lower())

#function to get count of all words in the text-file
WORDS_Cnt = Counter(words(eng_file))

#collect all words generated from input-word edits which are present in text
def known(words):
	return set([w for w in words if w in WORDS_Cnt])
#get word occurance probability
def prob(word):
	return WORDS_Cnt[word]/sum(WORDS_Cnt.values())
# get all words from one and two edits from given word 
def candidates(word):
	return known([word]) or known(edits1(word)) or known(edits2(word)) or [word] 
#get the correction 
def correction(word):
	return max(candidates(word),key=prob)

word = "the"
while True:
	word = input('Enter a Word :')
	print(correction(word))

