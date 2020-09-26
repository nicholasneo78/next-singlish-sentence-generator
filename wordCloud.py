#Code to generate word cloud

#Importing related modules
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 
import string
from PIL import Image
import numpy as np

#Functions

# load doc into memory
def load_doc(filename):
    # open the file as read only
    file = open(filename, 'r')
    # read all text
    text = file.read()
    # close the file
    file.close()
    return text

# turn a doc into clean tokens
def clean_doc(doc):
    # replace '--' with a space ' '
    doc = doc.replace('--', ' ')
    # split into tokens by white space
    tokens = doc.split()
    # remove punctuation from each token
    table = str.maketrans('', '', string.punctuation)
    tokens = [w.translate(table) for w in tokens]
    # remove remaining tokens that are not alphabetic
    tokens = [word for word in tokens if word.isalpha()]
    # make lower case
    tokens = [word.lower() for word in tokens]
    return tokens

# for google drive & smaller dataset
filename = './next-sentence-predictor/finalData/dataBatch2.txt'

doc = load_doc(filename)

# clean document and divide the words into tokens
tokens = clean_doc(doc)
print('Total Tokens: %d' % len(tokens))
print('Unique Tokens: %d' % len(set(tokens)))

#Create comment words
comment_words = " ".join(tokens)+" "
stopwords = set(STOPWORDS) 
print(stopwords)

#Set mask
mask = np.array(Image.open('./next-sentence-predictor/singaporeMap.jpg'))


#Create a word cloud
wc = WordCloud(stopwords=STOPWORDS,
               mask=mask, background_color="pink",
               max_words=2000, max_font_size=256,
               random_state=42, width=mask.shape[1],
               height=mask.shape[0]).generate(comment_words)


# plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wc) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show() 