"""
@author: Nicolas R.
(c) 2020

"""
from featureExtraction import textProcessing
from featureExtraction import tdIdf
from featureExtraction import coOccurrence
from featureExtraction import stylometry
from featureExtraction import sentimentAnalysis
from featureExtraction import vectorAnalysis
from featureExtraction import graphAnalysis


def printAllInfo(documents):
    """
    Function to print all collected information with the use of extraction functions.
    Used as a blueprint for later db or csv writers.
    :param documents: documents = {filename: object with extracted info}
    :return:
    """
    td_idf = tdIdf.getTFIDF(documents)

    for document in documents:
        #print basic info
        printHelper("Basic Info")
        print("Title: ")
        print(documents[document].title)
        print("Author: ")
        print(documents[document].author)
        print("Year of the publication: ")
        print(documents[document].year)
        print("Publisher: ")
        print(documents[document].publisher)

        #get cooccurences of a specific word
        printHelper("Cooccurrences of  word || range = 5 ")

        print("word = Frauen\n")
        if not documents[document].features["coOccurencesFrauen"]:
            print("Word doesn't appear in this document.")
        else:
            for line in documents[document].features["coOccurencesFrauen"]:
                print(line)


        print("\nword = Wahlrecht\n")

        if not documents[document].features["coOccurencesWahlrecht"]:
            print("Word doesn't appear in this document.")
        else:
            for line in documents[document].features["coOccurencesWahlrecht"]:
                print(line)

        print("\nword = Sozialismus\n")

        if not documents[document].features["coOccurencesSozialismus"]:
            print("Word doesn't appear in this document.")
        else:
            for line in documents[document].features["coOccurencesSozialismus"]:
                print(line)

        #sentiment analysis
        printHelper("SentimentAnalysis:")
        print("Sentiment around cooccurrences of word - Frauen -: ")
        print(documents[document].features["sentCoocFrauen"])
        print("\nSentiment around cooccurrences of word - Wahlrecht -: ")
        print(documents[document].features["sentCoocWahlrecht"])
        print("\nSentiment around cooccurrences of word - Sozialismus -: ")
        print(documents[document].features["sentCoocSozialismus"])
        print("\nSentiment of whole text: ")
        print(documents[document].features["sentText"])

        #tdIdf
        printHelper("TD-IDF")
        print("Frauen:")
        print(documents[document].features["tdIdfFrauen"]) #get returns None if word is not in document
        print("Wahlrecht:")
        print(documents[document].features["tdIdfWahlrecht"])

        #stylometry
        printHelper("Stylometry")
        print("Average word length: ")
        print(documents[document].features["styloWordLength"])

        #vector
        printHelper("Vector")
        print(documents[document].vector)

def printHelper(specification):
    """
    Prints a header.
    :param specification: the string which should be printed in the header
    :return:
    """
    print()
    print("#"*50)
    print(specification)
    print("#"*50)
    print()

def featureExtraction(documents):

    td_idf = tdIdf.getTFIDF(documents)
    range = 5

    for document in documents:
        documents[document].features["coOccurencesFrauen"] = coOccurrence.coOccurrences(documents[document], "Frauen", range)
        documents[document].features["sentCoocFrauen"] = sentimentAnalysis.sentAnalysis(documents[document].features["coOccurencesFrauen"],True)

        documents[document].features["coOccurencesWahlrecht"] = coOccurrence.coOccurrences(documents[document], "Wahlrecht", range)
        documents[document].features["sentCoocWahlrecht"] = sentimentAnalysis.sentAnalysis(documents[document].features["coOccurencesWahlrecht"],True)

        documents[document].features["coOccurencesSozialismus"] = coOccurrence.coOccurrences(documents[document], "Sozialismus", range)
        documents[document].features["sentCoocSozialismus"] = sentimentAnalysis.sentAnalysis(documents[document].features["coOccurencesSozialismus"],True)

        documents[document].features["sentText"] = sentimentAnalysis.sentAnalysis(documents[document].text,False)
        documents[document].features["tdIdfFrauen"] = td_idf[document].get("Frauen")
        documents[document].features["tdIdfWahlrecht"] = td_idf[document].get("Wahlrecht")
        documents[document].features["styloWordLength"] = stylometry.averageWordLength(documents[document])


if __name__ == '__main__':

    dataPath = "korpus/"
    documents = textProcessing.getAllTexts(dataPath) #documents = {filename: object with extracted info}

    featureExtraction(documents)
    vectorAnalysis.createVector(documents)
    distances = vectorAnalysis.euclideanDistance(documents)
    graph = graphAnalysis.createGraph(distances)
    #graphAnalysis.writeGraphToJson(graph)

    printAllInfo(documents)







