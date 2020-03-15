"""
@author: Nicolas R.
(c) 2020

"""

import numpy as np
import nltk
from nltk import bigrams
import itertools
import pandas as pd


def coOccurrenceMatrix(document):

    text = document.text.replace("\n"," ").split(" ")

    vocab = set(text)
    vocab = list(vocab)

    vocab_index = {word: i for i, word in enumerate(vocab)}

    # Create bigrams from all words in corpus
    bi_grams = list(bigrams(text))

    # Frequency distribution of bigrams ((word1, word2), num_occurrences)
    bigram_freq = nltk.FreqDist(bi_grams).most_common(len(bi_grams))

    # Initialise co-occurrence matrix
    # co_occurrence_matrix[current][previous]
    co_occurrence_matrix = np.zeros((len(vocab), len(vocab)))

    # Loop through the bigrams taking the current and previous word,
    # and the number of occurrences of the bigram.
    for bigram in bigram_freq:
        current = bigram[0][1]
        previous = bigram[0][0]
        count = bigram[1]
        pos_current = vocab_index[current]
        pos_previous = vocab_index[previous]
        co_occurrence_matrix[pos_current][pos_previous] = count
    co_occurrence_matrix = np.matrix(co_occurrence_matrix)

    # return the matrix and the index
    return co_occurrence_matrix, vocab_index

def printMatrix(document):

    matrix, vocab_index = coOccurrenceMatrix(document)
    data_matrix = pd.DataFrame(matrix, index=vocab_index,
                           columns=vocab_index)


    data_matrix.to_csv("coocMatrix.csv", sep='\t')
    #print(data_matrix)

# Create one list using many lists
#data = list(itertools.chain.from_iterable(text_data))


