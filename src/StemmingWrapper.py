"""
@author Axel Ancona Esselmann
"""

from nltk.stem.lancaster import LancasterStemmer

class StemmingWrapper():
    def __init__(self):
        pass

    def stem(self, token):
        stemmer = LancasterStemmer();
        return stemmer.stem(token);
