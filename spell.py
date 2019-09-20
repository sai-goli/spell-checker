import string
import re
from collections import Counter

LETTERS = string.ascii_lowercase

def edits1(word):
	n = len(word)
	del_ = [word[:i]+word[i+1:]  for i in range(len(word))]
	ins_ = [word[:i]+letter+word[i:] for i in range(len(word)+1) for letter in LETTERS] 
	sub_ = [word[:i]+letter+word[i+1:] for i in range(len(word)) for letter in LETTERS]
	swap_ = [word[:i]+word[i+1]+word[i]+word[i+2:] for i in range(len(word)-1)] 
	all_edits = set(del_+ins_+sub_+swap_)
	#print('#del_',len(del_),n)
	#print('#ins_',len(ins_),26*(n+1))
	#print('#sub_',len(sub_),26*n)
	#print('#swap_',len(swap_),n-1)
	return all_edits
def edits2(word):
	return set( w2 for w1 in edits1(word) for w2 in edits1(w1))

eng_file = open('big.txt').read()

def words(text):
	return re.findall(r'\w+',text.lower())

WORDS_Cnt = Counter(words(eng_file))


def known(words):
	return set([w for w in words if w in WORDS_Cnt])

def prob(word):
	return WORDS_Cnt[word]/sum(WORDS_Cnt.values())

def candidates(word):
	return known([word]) or known(edits1(word)) or known(edits2(word)) or [word] 

def correction(word):
	return max(candidates(word),key=prob)

word = "the"

while True:
	word = input('Enter a Word :')
	print(correction(word))

