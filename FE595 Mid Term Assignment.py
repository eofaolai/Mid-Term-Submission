#!/usr/bin/env python
# coding: utf-8

# In[35]:


#reference https://stackabuse.com/python-for-nlp-developing-an-automatic-text-filler-using-n-grams/
import re
import nltk
import random

#use ngram model to predict reconstruct meaning from the Luckin Coffee Inc Q3 2019 Earnings call
#The company recently disclose misconduct in revenue reporting


with open('/Users/Midnight/2019-Nov-13-LK.OQ-139494797335-Transcript.txt', 'r', encoding="utf8", errors='ignore') as f:
    file_contents = f.read()
#print(file_contents)

file_contents = file_contents.lower()
file_contents = re.sub(r'[^A-Za-z. ]', '', file_contents)
#file_contents = re.split('\s', file_contents)
#file_contents = file_contents.replace(" .", ".")
#file_contents = re.sub(r'\s([?.!"](?:\s|$))', r'\1', file_contents)

# User: select and generate the ngrams model and store it in ngrams varible
ngrams = {}
#words = 5
words = input('Enter the number of words from which to generate the ngram model: ')
words = int(words)

words_tokens = nltk.word_tokenize(file_contents)
for i in range(len(words_tokens)-words):
    seq = ' '.join(words_tokens[i:i+words])
    seq = re.sub(r'\s([?.!"](?:\s|$))', r'\1', seq)
    print(seq)
    if  seq not in ngrams.keys():
        ngrams[seq] = []
    ngrams[seq].append(words_tokens[i+words])


#prediction the text from user input from the available text
print("")
print("")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Above is list of ngrams that you can insert below to predict the text")
print("One ironical example is 'risks which are more specifically' ")
curr_sequence = input('Please enter the text for prediction (ensure you only type in the number of words specified to generate the ngram model):')

output = curr_sequence
for i in range(70):
    if curr_sequence not in ngrams.keys():
        break
    possible_words = ngrams[curr_sequence]
    next_word = possible_words[random.randrange(len(possible_words))]
    output += ' ' + next_word
    seq_words = nltk.word_tokenize(output)
    curr_sequence = ' '.join(seq_words[len(seq_words)-words:len(seq_words)])
    #curr_sequence = re.sub(r'\s([?.!"](?:\s|$))', r'\1', curr_sequence)
    

#output = output.replace(" .", ".")
print("")
print("")

print("The predicted output based on what you entered is displayed below")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(output)


# In[ ]:





# In[1]:


print(seq)


# In[27]:


import re

test_str = "Some Co Inc. Other Co L.P."

print(re.split('\s', test_str))


# In[ ]:




