import unittest
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    import io;
    sys.path.append(path.abspath(path.join(__file__, "..", "..")))

from src.Tokenizer import Tokenizer;
from src.VirtualDocumentCollection import VirtualDocumentCollection;
from src.AlphanumericWhiteSpaceList import AlphanumericWhiteSpaceList;
from src.LowerCaseNormalizer import LowerCaseNormalizer;
from src.Testing import *

class TokenizerTest(unittest.TestCase):
    def _getTestFileName(self):
        fileName = path.dirname(path.realpath(__file__)) + path.sep + 'TokenizerTestData' + path.sep + 'f1.txt';
        return fileName;

    def dataProvider_nextToken(self):
        return [
            [ 1, 'this'],
            [ 2, '1234'],
            [ 3, 'is_a_test'],
            [ 4, None]
        ]

    @dataProvider(dataProvider_nextToken)
    def test_nextToken(self, repeat, token):
        docCollection = VirtualDocumentCollection(self._getTestFileName());
        doc           = docCollection.nextDocument();
        wsList        = AlphanumericWhiteSpaceList();
        normalizer    = LowerCaseNormalizer();
        tokenizer     = Tokenizer(wsList, normalizer);
        tokenizer.loadDocument(doc);
        for n in xrange(0,repeat):
            result, tokenPosition = tokenizer.nextToken();
        self.assertEqual(result, token);

if __name__ == '__main__':
    unittest.main()