# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 10:30:53 2017

@author: atul.kumar
"""


from nltk.tokenize import RegexpTokenizer
#from stop_words import get_stop_words
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import pandas as pd
import pyLDAvis.gensim as gensimvis
import pyLDAvis
import numpy as np
tokenizer = RegexpTokenizer(r'\w+|\d+')

# create English stop words list
stop_words = set(stopwords.words('english'))
stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}','following','t','00','fi','wi','ny','3','17','7','4','mt','5','2','2017','issues','new','ny','one','now','fl','ca','ip','0','10','8','t','00','2','please','number','get','issue','since','working','us','part','added','need'])
#en_stop = get_stop_words('en')
#en_stop.append('.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}','following','t','00','fi','wi','ny','3','17','7','4','mt','5','2','2017','issues','new','ny','one','now','fl','ca','ip','0','10','8','t','00','2','please','number','get')
#en_stop =en_stop.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}','following','t','00','fi','wi','ny','3','17','7','4'])
# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()
#dictn = ['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}','following','t','00','fi','wi','ny','3','17','7','4','mt','5','2','2017','issues','new','ny','one','now','fl','ca','ip','0','10','8','t','00','2','please','number','get']    
# create sample documents
location = r'E:\AT&T\code\Combined.csv'
df = pd.read_csv(location, names=None)
df['subject'] = df['subject'].astype(str)
#texts = df[df['subject'].notnull()]
doc_set = df['subject'].tolist()
# compile sample documents into a list
#doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]

# list for tokenized documents in loop
texts = []

# loop through document list
for i in doc_set:
    
    # clean and tokenize document string
    raw = i.lower()
    for word in raw.split():
        if (word != '4g') or (word != '3g'):
            #raw = ''.join(word)
            raw = ''.join(map(lambda c: '' if c in '0123456789' else c, raw))
            #print raw
        else:
            raw = ''.join(word)
            #print raw
    tokens = tokenizer.tokenize(raw)
    #print tokens
    #print tokens
    tokens = custom_dict(tokens)
    #print(token) 
    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in stop_words]

    # add tokens to list
    texts.append(stopped_tokens)
    
def custom_dict(token):
   d = {'3g':'provisioning','sim':'provisioning'}
   #token = token
   #print token
   counter = 0
   for t in token:
       for key in d:
           if key==t:
               token[counter]=d[key]
               print t
               print d[key]
       counter = counter + 1        
   return token
    
# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)
    
# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]
SOME_FIXED_SEED = 42

# before training/inference:
np.random.seed(SOME_FIXED_SEED)
# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=8, id2word = dictionary, passes=200)


#vis_data = gensimvis.prepare(ldamodel, corpus, dictionary)
#pyLDAvis.show(vis_data)
#topic_word = ldamodel.topic_word
#n_top_words = 8
#for i, topic_dist in enumerate(topic_word):
    ##topic_words = np.array(vocab)[np.argsort(topic_dist)][:-n_top_words:-1]
    #print('Topic {}: {}'.format(i, ' '.join(topic_words)))
    
#print(ldamodel.print_topics(num_topics=3, num_words=3))    
#outpth = r'C:/Users/atul.kumar/'
#pyLDAvis.save_html(vis_data,outpth+'LDA_Visualization.html')