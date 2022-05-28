def read_file_content(filename):
# [assignment] Add your code here
with open(filename) as f:
  contents = f.read()
return contents
 
def count_words():
 text = read_file_content ("./story.txt")
 words_list = text.split()
 
 
 counter = {}
 for word in words_list:
  word = word.lower()
  if word in counter:
   counter[word] += 1
 else:
  counter[word] =1
 
 return counter
 
print (count_words())