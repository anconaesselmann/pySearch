"""
@author Axel Ancona Esselmann
"""
class StopWordList():
    _stopWords = None;
    def __init__(self):
        self._stopWords = frozenset(['the', 'is', 'at', 'of', 'on', 'and', 'a']);

    def isStopWord(self, token):
        return token in self._stopWords;
