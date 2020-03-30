"""
@author: Nicolas R.
(c) 2020

"""
import networkx as nx
from networkx.readwrite import json_graph
import json

def createGraph(distances):
    """
    Creating networkx graph out of the distances as weights of the edges
    :param distances:  a list of tuples (text,text,distance)
    :return: networkx graph
    """
    G = nx.Graph()
    G.add_weighted_edges_from(distances)

    return G

def writeGraphToJson(graph):
    graphJson = json_graph.node_link_data(graph)
    with open("graphVis/graph.json", 'w') as f:
        json.dump(graphJson, f, indent=4)

def writeGraphToGml(graph):
    nx.write_gml(graph,"graphVis/graph.gml")