"""
@author: Nicolas R.
(c) 2020

"""
import os
import textProcessing
import tdIdf

dataPath = "korpus/"
documents = textProcessing.getAllTexts(dataPath)

td_Idf = tdIdf.getTFIDF(documents)







