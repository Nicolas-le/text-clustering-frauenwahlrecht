import string
import numpy as np
from collections import defaultdict


def getTFIDF(documents):
    '''
    The first iteration computes all documents and creates the dictionary t.
    t contains for every word a dictionary of all docs it appears in the count.

    The second iteration iterates t and calculates the TFIDF with a little helper-func.

    t =     pre-dictionary used for the first iteration to get the total number of docs a token appears in.
    N =     number of documents in corpus
    dk =    count of documents a token appears in
    D =     length of the specific document

    :param documents:   All documents of the corpus
    :return:            dictionary with all documents and the tdidf for every token
    '''


    tfidf = defaultdict(dict)
    t = defaultdict(dict)
    N = len(documents)

    for doc in documents:

        doc = doc.text.replace("\n"," ").split(" ")
        for word in doc:
            print(word)

            word = word.translate(str.maketrans('', '', string.punctuation)) #removes punctuatiopn
            count = t[word].get(doc,0)
            t[word][doc] = count + 1

    for word in t:
        dk = len(t[word])
        for doc in t[word]:
            D = len(documents[doc])
            wordFreq = t[word][doc]
            tfidf[doc][word] = calculateTFIDF(N,dk,wordFreq,D)

    return tfidf


def calculateTFIDF(N,dk,wordFreq,D):
    '''
    Calculates the TFIDF.
    :param N:           number of documents in corpus
    :param dk:          count of documents a token appears in
    :param wordFreq:    How often the token appears in the specific document
    :param D:           length of the specific document
    :return:
    '''
    tf = wordFreq/D
    idf = np.log(N/dk)+1 #I took the formula out of our lecture script

    return tf*idf