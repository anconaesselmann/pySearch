"""
@author Axel Ancona Esselmann
"""
from time import time;
class Timing():
    _displayText = False;
    def __init__(self, displayText = False):
        self._displayText = displayText;

    def out(self, text):
        if self._displayText: print text;

    def start(self):
        self._start = time();

    def stop(self):
        self._stop = time();
        self._elapsed = self._stop - self._start;
        return self._elapsed;