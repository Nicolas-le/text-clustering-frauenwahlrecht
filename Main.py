"""
@author: Nicolas R.
(c) 2020

"""
from featureExtraction import textProcessing
from featureExtraction import tdIdf
from featureExtraction import coOccurrence
from featureExtraction import stylometry
from featureExtraction import sentimentAnalysis




def printAllInfo(documents):
    td_idf = tdIdf.getTFIDF(documents)

    for file in documents:
        #print basic info
        printHelper("Basic Info")
        print("Title: ")
        print(documents[file].title)
        print("Author: ")
        print(documents[file].author)
        print("Year of the publication: ")
        print(documents[file].year)

        #get cooccurences of a specific word
        printHelper("Cooccurrences of word")
        word = "Frauen"
        range = 5
        print("word: "+ word +" range: "+ str(range))
        coOccurences = coOccurrence.coOccurrences(documents[file], word, range)
        print(coOccurences)

        #sentiment analysis
        printHelper("SentimentAnalysis:")
        print("Sentiment around cooccurrences: ")
        print(sentimentAnalysis.sentAnalysis(coOccurences,True))
        print("Sentiment of whole text: ")
        print(sentimentAnalysis.sentAnalysis(documents[file].text,False))

        #tdIdf
        printHelper("TD-IDF of Frauen")
        print(td_idf[file].get("Frauen")) #get returns None if word is not in file

        #stylometry
        printHelper("Stylometry")
        print("Average word length: ")
        print(stylometry.averageWordLength(documents[file]))

def printHelper(specification):
    print()
    print("#"*50)
    print(specification)
    print("#"*50)
    print()

if __name__ == '__main__':

    dataPath = "korpus/"
    documents = textProcessing.getAllTexts(dataPath) #documents = {filename: object with extracted info}

    printAllInfo(documents)






