"""
@author: Nicolas R.
(c) 2020

"""
import os
import textProcessing
import tdIdf

dataPath = "korpus/"
documents = textProcessing.getAllTexts(dataPath)

#documents = {filename: object with extracted info}

td_Idf = tdIdf.getTFIDF(documents)

for file in documents:
    print(file)
    print(td_Idf[file]["ist"])
    #add function if word isn't in file







