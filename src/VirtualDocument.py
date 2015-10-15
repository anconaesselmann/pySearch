"""
Used by Virtual Document Collection to turn sections of a file into individual file streams
to simulate different documents. Can be swapped out with actual streams.
@author Axel Ancona Esselmann
"""

import io;
from src.Document import Document

class VirtualDocument(Document):
    _documentName = None;
    _filePointer  = None;
    _last_pos     = None;
    _eof          = False;

    def __init__(self, filePointer, docName):
        self._documentName = docName;
        self._filePointer  = filePointer;
        self._currentPosition = -1;

    def getName(self):
        return self._documentName;

    def isEOF(self):
        return self._eof;

    def getChar(self):
        self.last_pos = self._filePointer.tell();
        char = self._filePointer.read(1);
        if char == '<':
            if self._filePointer.read(5) == '/DOC>':
                self._eof = True;
                return '';
            else:
                self._filePointer.seek(self.last_pos);
                char = self._filePointer.read(1);
        self._currentPosition += 1;
        return char;

    def ungetChar(self):
        self._filePointer.seek(self.last_pos);
        self._currentPosition -= 1;

    def tell(self):
        return self._currentPosition;