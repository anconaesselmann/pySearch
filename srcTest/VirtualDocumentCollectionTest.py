import unittest
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.abspath(path.join(__file__, "..", "..")))

from src.VirtualDocumentCollection import VirtualDocumentCollection
from src.Testing import *

class VirtualDocumentCollectionTest(unittest.TestCase):

    def dataProvider_getDocumentText(self):
        return [
            [ 1, 'docName_1', 'This is text\n' ],
            [ 2, 'docName_2', 'document 2 text\n' ],
            [ 3, 'docName_3', 'document <DOC>3 text\n' ],
            [ 4,  None, None]
        ]

    @dataProvider(dataProvider_getDocumentText)
    def test_getDocumentText(self, repeat, docName, docText):
        # Given a text file with documents separated by tags
        fileName   = path.dirname(path.realpath(__file__)) + path.sep + 'VirtualDocumentCollectionTestData' + path.sep + 'documents.txt';
        docCollect = VirtualDocumentCollection(fileName);

        # When nextDocumet is called a given time
        for n in xrange(0,repeat):
            text = None;
            document = docCollect.nextDocument();
            if document is not None:
                text = '';
                char = document.getChar();
                while char != '':
                    text += char;
                    char = document.getChar();
        # Then getName should return the correct document name and the document text should be retrievable with getChar()
        if document is not None: self.assertEqual(docName, document.getName());
        self.assertEqual(docText, text);

    def test_ungetChar(self):
        fileName   = path.dirname(path.realpath(__file__)) + path.sep + 'VirtualDocumentCollectionTestData' + path.sep + 'documents.txt';
        docCollect = VirtualDocumentCollection(fileName);
        document = docCollect.nextDocument();
        char = document.getChar();
        document.ungetChar();
        char = document.getChar();

        self.assertEqual(char, 'T');

if __name__ == '__main__':
    unittest.main()