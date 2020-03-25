from textblob_de import TextBlobDE as tb

def sentAnalysis(source, isCoOc):
    """
    Polarity is float which lies in the range of [-1,1] where 1 means positive statement and -1
    means a negative statement. Subjective sentences generally refer to personal opinion,
    emotion or judgment whereas objective refers to factual information. Subjectivity is
    also a float which lies in the range of [0,1].

    :param source: This is the source for which the sentiment should be calculated
    :param isCoOc: if True: The source is a list of already tokenized cooccurrences connected to some word
                    if False: this already the whole text as a string
    :return:       blob.sentiment as Sentiment(polarity=x, subjectivity=<0.3333333333333333>)

    """

    if isCoOc:
        blob = tb(listToString(source))
    else:
        blob = tb(source)

    return blob.sentiment


def listToString(coOccurrences):

    string = ""
    #textblob can only process strings, tokenization is done by itself
    for coOc in coOccurrences:
        string += " " + ' '.join(coOc)

    return string