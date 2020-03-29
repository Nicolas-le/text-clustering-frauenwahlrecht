"""
@author: Nicolas R.
(c) 2020

"""
import numpy
import networkx as nx
import matplotlib.pyplot as plt

def createVector(documents):
    """
    vector:
    0 sent text pol,
    1 sent text subj,
    2 sent cooc "Frauen" pol,
    3 sent cooc Frauen subj,
    4 td-idf "Frauen",
    5 td-idf "Wahlrecht", (if none --> 0)
    6 stilo word length
    :param documents: document dictionary
    :return:
    """

    for document in documents:
        documentVector = [0,0,0,0,0,0,0]

        documentVector[0] = documents[document].features["sentText"].polarity
        documentVector[1] = documents[document].features["sentText"].subjectivity
        documentVector[2] = documents[document].features["sentCooc"].polarity
        documentVector[3] = documents[document].features["sentCooc"].subjectivity

        if documents[document].features["tdIdfFrauen"] == None:
            documentVector[4] = 0
        else:
            documentVector[4] = documents[document].features["tdIdfFrauen"]

        if documents[document].features["tdIdfWahlrecht"] == None:
            documentVector[5] = 0
        else:
            documentVector[5] = documents[document].features["tdIdfWahlrecht"]


        documentVector[6] = documents[document].features["styloWordLength"]

        documents[document].vector = tuple(documentVector)



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

            distances.append((document,doc,dist*10))
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

    createGraph(distances)


def createGraph(distances):
    """
    Creating networkx graph out of the distances as weights of the edges
    :param distances:  a list of tuples (text,text,distance)
    :return:
    """
    GTMP = nx.Graph()
    GTMP.add_weighted_edges_from(distances)

    #printGraph(GTMP)
    nx.write_gml(GTMP,"graph.gml")

def printGraph(G):
    """
    Quick graph printer. Will be removed later
    :param G: networkx graph
    :return:
    """

    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 10]
    emedium = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 5 < 10]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 5]
    etiny = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] == 1]


    pos = nx.circular_layout(G)

    nx.draw_networkx_nodes(G, pos, node_size=300)

    # edges
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=5)
    nx.draw_networkx_edges(G, pos, edgelist=esmall, width=1,edge_color='r')
    nx.draw_networkx_edges(G, pos, edgelist=emedium, width=3)
    nx.draw_networkx_edges(G, pos, edgelist=etiny, width=1,style='dashed',edge_color='b')


    # labels
    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

    #plt.savefig('graph.png',dpi=300,format = 'png',bbox_inches = 'tight',pad_inches = 0.3)
    plt.show()

