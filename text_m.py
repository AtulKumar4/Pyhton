# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 15:11:43 2017

@author: atul.kumar
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import numpy as np
from itertools import combinations
from random import shuffle
import pandas as pd

def majorclust_sklearn():    
    location = r'E:\AT&T\code\Combined.csv'
    df = pd.read_csv(location, names=None)
    df['subject'] = df['subject'].astype(str)
    #texts = df[df['subject'].notnull()]
    texts = df['subject'].tolist()
    vectorizer = TfidfVectorizer()
    corpus_mat = vectorizer.fit_transform(texts)
    num_of_samples, num_of_features = corpus_mat.shape

    cosine_distances = np.zeros((num_of_samples, num_of_samples))
    for i in range(len(texts)):
        cosine_distances[i] = linear_kernel(corpus_mat[i:i+1], corpus_mat).flatten()
        cosine_distances[i, i] = 0

    t = False
    indices = np.arange(num_of_samples)
    while not t:
        t = True
        shuffled_indices = np.arange(num_of_samples)
        shuffle(shuffled_indices)
        for index in shuffled_indices:
            # aggregating edge weights 
            new_index = np.argmax(np.bincount(indices, 
                                              weights=cosine_distances[index]))
            if indices[new_index] != indices[index]:
                indices[index] = indices[new_index]
                t = False

    clusters = {}
    for index, target in enumerate(indices):
        clusters.setdefault(target, []).append(texts[index])

    for cluster in clusters:
        print(80*"=")
        print("\n".join(clusters[cluster]))
    return clusters

def main(args):
    #documents = get_documents()
    #add_tfidf_to(documents)
    #dist_graph = get_distance_graph(documents)

    for cluster in majorclust_sklearn():
        print "========="
        for doc_id in cluster:
            print documents[doc_id]["text"]


if __name__ == '__main__':
    main(sys.argv)