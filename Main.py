"""
@author: Nicolas R.
(c) 2020

"""
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

        coOccurences = coOccurrence.coOccurrences(documents[file], "Frauen",10)
        print(coOccurences)
        #print(sentimentAnalysis.sentAnalysis(documents[file].text,False))
        #print(sentimentAnalysis.sentAnalysis(coOccurences,True))



    """
    coOccurences = coOccurrence.coOccurrenceMatrix(documents["korpus/baader_arbeit_1911.tcf.xml"], "Frauen")

    td_idf = tdIdf.getTFIDF(documents)

    for file in documents:
        #print(stylometry.averageWordLength(documents[file]))
        
    """

def getAll(documents):
    td_idf = tdIdf.getTFIDF(documents)


    for file in documents:
        #print basic info
        print(documents[file].title)
        print(documents[file].author)
        print(documents[file].year)

        #get cooccurences of a specific word
        word = "Frauen"
        range = 10
        coOccurences = coOccurrence.coOccurrences(documents[file], word, 5)
        print(sentimentAnalysis.sentAnalysis(coOccurences,True))

        print(sentimentAnalysis.sentAnalysis(documents[file].text,False))

        #tdIdf
        print(td_idf[file].get("Frauen"))



"""
printer for ididf
for file in documents:

    print(td_idf[file].get("Frauen")) #get returns None if word is not in file
    print()
"""






