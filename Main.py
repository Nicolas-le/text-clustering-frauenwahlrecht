"""
@author: Nicolas R.
(c) 2020

"""
import os
import textProcessing

dataPath = "korpus/"
texts = textProcessing.getAllTexts(dataPath)

for t in texts:
    print(t.author)



