"""
Used in conjunction with VirtualDocument. See description there.

@author Axel Ancona Esselmann
"""

import io;
from src.VirtualDocument import VirtualDocument

class VirtualDocumentCollection():
    _documents      = None;
    _currentDocName = None;
    _hasMoreDocuments = True;
    _fileName         = None;

    def __init__(self, fileName):
        self._fileName  = fileName;
        self.reset();

    def reset(self):
        self._documents = io.open(self._fileName, 'r');

    def _getNextDocName(self):
        char = None;
        while char != '':
            char = self._documents.read(1);
            if char == '<':
                docTag = self._documents.read(4);
                if docTag == 'DOC ':
                    nextChar = self._documents.read(1);
                    docName  = '';
                    while nextChar != '>' and nextChar != '':
                        docName += nextChar;
                        nextChar = self._documents.read(1);
                    self._documents.read(1); # remove line break
                    return docName;
    def hasMoreDocuments(self):
        return self._hasMoreDocuments;

    """ retrieves the next document
    returns: VirtualDocument
    """
    def nextDocument(self):
        self._currentDocName = self._getNextDocName();
        vDoc = VirtualDocument(self._documents, self._currentDocName);
        if vDoc.getName() is None:
            self._hasMoreDocuments = False;
            return None;
        else: return vDoc;
