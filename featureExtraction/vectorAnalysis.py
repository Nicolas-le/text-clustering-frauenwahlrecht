"""
@author: Nicolas R.
(c) 2020

"""

def createVector(documents):

    """vector:
    sent text pol,
    sent text subj,
    sent cooc "Frauen" pol,
    sent cooc Frauen subj,
    td-idf "Frauen",
    td-idf "Wahlrecht", (if none --> 0)
    stilo word length
    """
    for file in documents:
        filevector = (0,0,0,0,0,0,0)

        sentText = sentimentAnalysis.sentAnalysis(documents[file].text,False)[0]




def euclideanDistance():
    print()

def createGraph():
    print()

