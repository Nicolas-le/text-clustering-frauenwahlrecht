"""
@author: Nicolas R.
(c) 2020

"""


def averageWordLength(document):

    text = document.text.replace("\n"," ").replace("- ","").split(" ")
    average = sum(len(word) for word in text) / len(text)

    return average

