import re
import string
freq = {}
document_text = open('abc.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
 
for word in match_pattern:
    count = freq.get(word,0)
    freq[word] = count + 1
     
freq_list = freq.keys()
 
for words in freq_list:
    print (words, freq[words])
