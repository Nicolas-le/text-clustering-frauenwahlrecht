"""
@author: Nicolas R.
(c) 2020

"""
from nltk import ngrams


def coOccurrenceMatrix(document,word):

    text = document.text.replace("\n"," ").replace("- ","").split(" ")

    ninegrams = ngrams(text,9)

    cooc = []

    for gram in ninegrams:
        if gram[4] == word:
            cooc.append(gram)

    return cooc

