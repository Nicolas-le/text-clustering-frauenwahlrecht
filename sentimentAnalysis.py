from textblob_de import TextBlobDE as tb

def sentAnalysis(coOccurrences):

    blob = tb(coOccurrences)

    print(blob.sentiment)
