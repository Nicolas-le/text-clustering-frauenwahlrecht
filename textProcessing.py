import glob
import os
from bs4 import BeautifulSoup as bs

class text:
    title = ""
    author = ""
    year = 0
    text = ""
    publisher = ""


    def __init__(self,file):
        info = infoExtraction(file)
        self.title = info[0]
        self.author = info[1]
        self.year = info[2]
        self.text = info[3]



def infoExtraction(f):
    year = 0

    soup = bs(f, 'lxml')

    text = str(soup.find('text').text)
    title = str(soup.find('cmdp:title').text)
    author = str(soup.find('cmdp:surname').text) + ", "+ str(soup.find('cmdp:forename').text)

    #publisher = soup.find('cmdp:publisher')



    print(author)
    print(title)
    #print(publisher)
    print(year)
    print()

    return [title,author, year, text]

def getAllTexts(path):

    for filename in glob.glob(os.path.join(path, '*.xml')):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            infoExtraction(f)

