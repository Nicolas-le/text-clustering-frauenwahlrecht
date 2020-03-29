"""
@author: Nicolas R.
(c) 2020

"""

import glob
import os
from bs4 import BeautifulSoup as bs
import numpy

class text:
    title = ""
    author = ""
    year = 0
    text = ""
    publisher = ""
    vector = ()
    features = {}


    def __init__(self,file):
        info = infoExtraction(file)
        self.title = info[0]
        self.author = info[1]
        self.year = info[2]
        self.publisher = info[3]
        self.text = info[4]
        self.vector = ()
        self.features = {}

def infoExtraction(file):
    """
    Extracts the information out of the given file.
    :param file:
    :return:
    """

    soup = bs(file, 'lxml')

    author = str(soup.find('cmdp:surname').text) + ", "+ str(soup.find('cmdp:forename').text)
    year = soup.find_all('cmdp:date',type="publication")[1].text
    title = str(soup.find('cmdp:title').text)

    if len(soup.find_all('cmdp:publisher')) > 1:
        publisher = str(soup.find_all('cmdp:publisher')[1].text)
    else:
        publisher = "Nicht bekannt."

    text = str(soup.find('text').text)


    return [title,author, year, publisher, text]

def getAllTexts(path):
    texts = {}

    for filename in glob.glob(os.path.join(path, '*.xml')):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            texts[filename] = text(f)

    return texts

