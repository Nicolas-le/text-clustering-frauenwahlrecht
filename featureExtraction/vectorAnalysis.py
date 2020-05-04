"""
@author: Nicolas R.
(c) 2020

"""
import numpy


def createVector(documents):
    """
    vector:
    0 sent text pol,
    1 sent text subj,
    2 sent cooc "Frauen" pol,
    3 sent cooc "Frauen" subj,
    4 sent cooc "Wahlrecht" pol,
    5 sent cooc "Wahrlrecht" subj,
    6 sent cooc "Wahlrecht" pol,
    7 sent cooc "Wahrlrecht" subj,
    4 td-idf "Frauen",
    5 td-idf "Wahlrecht", (if none --> 0)
    6 stilo word length
    :param documents: document dictionary
    :return:
    """

    for document in documents:
        documentVector = [0,0,0,0,0,0,0,0,0,0,0]

        documentVector[0] = documents[document].features["sentText"].polarity
        documentVector[1] = documents[document].features["sentText"].subjectivity
        documentVector[2] = documents[document].features["sentCoocFrauen"].polarity
        documentVector[3] = documents[document].features["sentCoocWahlrecht"].subjectivity

        documentVector[4] = documents[document].features["sentCoocWahlrecht"].polarity
        documentVector[5] = documents[document].features["sentCoocWahlrecht"].subjectivity

        documentVector[6] = documents[document].features["sentCoocWahlrecht"].polarity
        documentVector[7] = documents[document].features["sentCoocWahlrecht"].subjectivity

        if documents[document].features["tdIdfFrauen"] == None:
            documentVector[8] = 0
        else:
            documentVector[8] = documents[document].features["tdIdfFrauen"]

        if documents[document].features["tdIdfWahlrecht"] == None:
            documentVector[9] = 0
        else:
            documentVector[9] = documents[document].features["tdIdfWahlrecht"]


        documentVector[10] = documents[document].features["styloWordLength"]

        documents[document].vector = tuple(documentVector)
        #documents[document].vector = documentVector



def euclideanDistance(documents):
    """
    Calculates the euclidean distance between the document vectors.
    creates list of edges aka. distances : (document,document,distance)
    :param documents:
    :return:
    """
    #distances = (text,text,distance)

    distances = []

    for document in documents:
        for doc in documents:

            if document == doc:
                continue

            a = numpy.array(documents[document].vector)
            b = numpy.array(documents[doc].vector)

            dist = numpy.linalg.norm(a-b)

            #only really close distances
            if dist*10 < 2:
                distances.append((documents[document].author,documents[doc].author,dist*10))
            """    
            check if distance makes sense        
            print("Doc1: " +documents[document].title + " - " + documents[document].author)
            for i in documents[document].features:
                if i == "coOccurencesFrauen":
                    continue
                print(i)
                print(documents[document].features[i])
            print()
            print("Doc2: " +documents[doc].title + " - " + documents[doc].author)
            for i in documents[doc].features:
                if i == "coOccurencesFrauen":
                    continue
                print(i)
                print(documents[doc].features[i])
            print()
            print("Distance: " + str(dist*10))

            print("-"*50)"""

    return distances




