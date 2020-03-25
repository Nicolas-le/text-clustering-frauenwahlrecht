"""
@author: Nicolas R.
(c) 2020

"""
from nltk import ngrams


def coOccurrences(document,word,range):
    """
    Calculates the ngrams of the input text. Returns all the ngrams where
    the chosen word is in the middle.
    :param document:    document object. The attribute text is extracted and formated
    :param word:        the word the cooccurrence is wanted for
    :param range:       specifies how many words before and after the word should be
                        f.ex. range = 2 --> x,y,word,z,v
    :return:            returns a list of tokenized strings --> the cooccurrences
    """

    text = document.text.replace("\n"," ").replace("- ","").split(" ")

    range = range*2+1
    ninegrams = ngrams(text,range)

    cooc = []

    for gram in ninegrams:
        if gram[int(range/2)] == word:
            cooc.append(gram)

    return cooc

