"""
@author: Nicolas R.
(c) 2020

"""
import os
from featureExtraction import textProcessing
from featureExtraction import tdIdf
from featureExtraction import coOccurrence
from featureExtraction import stylometry
from featureExtraction import sentimentAnalysis


if __name__ == '__main__':

    dataPath = "korpus/"
    documents = textProcessing.getAllTexts(dataPath) #documents = {filename: object with extracted info}

    #coOccurences = coOccurrence.coOccurrenceMatrix(documents["korpus/baader_arbeit_1911.tcf.xml"], "Frauen")
    #sentimentAnalysis.sentAnalysis(coOccurences)


    for file in documents:

        coOccurences = coOccurrence.coOccurrences(documents[file], "Frauen")
        print(sentimentAnalysis.sentAnalysis(documents[file].text,False))
        print(sentimentAnalysis.sentAnalysis(coOccurences,True))



    """
    coOccurences = coOccurrence.coOccurrenceMatrix(documents["korpus/baader_arbeit_1911.tcf.xml"], "Frauen")

    td_idf = tdIdf.getTFIDF(documents)

    for file in documents:
        #print(stylometry.averageWordLength(documents[file]))
        
    """



"""
printer for ididf
for file in documents:
    print(documents[file].title)
    print(documents[file].author)
    print(documents[file].year)
    print(td_idf[file].get("Frauen")) #get returns None if word is not in file
    print()
"""






