"""
Tokenizes a document stream.

@author Axel Ancona Esselmann
"""

"""
Tokenizer returns advances through a document with nextToken() until the end of the document is reached
"""
class Tokenizer():
    def __init__(self, whiteSpaceList, normalizer):
        self._whitespaceList = whiteSpaceList;
        self._normalizer     = normalizer;
        self._document       = None;
        self._tokenDocumentPosition = None;
        self._tokenPosition = -1;

    def loadDocument(self, document):
        self._document = document;
        self._tokenPosition = -1;

    """
    Returns the next token from a Document or None when no more tokens are available.
    """
    def nextToken(self):
        self._skipWhitespace();
        if self._document.isEOF(): return None, None;
        self._tokenPosition += 1;
        char  = self._document.getChar();
        token = '';
        self._tokenDocumentPosition = self._document.tell();
        while char != '':
            if self._whitespaceList.isWhitespace(char): break;
            else: token += char;
            char = self._document.getChar();
        return self._normalizer.normalize(token), self._tokenDocumentPosition;

    def _skipWhitespace(self):
        whitespace = self._document.getChar();
        while self._whitespaceList.isWhitespace(whitespace):
            whitespace = self._document.getChar();
            if self._document.isEOF(): return;
        self._document.ungetChar();
        pass;
