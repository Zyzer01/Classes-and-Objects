def find_anagrams (word, anagram): 
""""
Find all anagrams of a word in a list of word.
"""

word = word.lower()
word = word.replace(" ", "")

anagram = anagram.lower()
anagram = anagram.replace(" ", "")

if sorted(anagram) == sorted (word):
  return True
else:
  return False
  
print(find_anagrams("hello", "check"))
print(find_anagrams("elbow", "below"))