import unittest
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.abspath(path.join(__file__, "..", "..")))

from src.Parser import Parser
from src.AlphanumericWhiteSpaceList import AlphanumericWhiteSpaceList;
from src.LowerCaseNormalizer import LowerCaseNormalizer;
from src.Tokenizer import Tokenizer;
from src.PartitionTable import PartitionTable;
from src.VirtualDocumentCollection import VirtualDocumentCollection;
from src.StemmingWrapper import StemmingWrapper
from src.StopWordList import StopWordList;

class ParserTest(unittest.TestCase):
    def test___init__(self):
        # parser = Parser(None, None);
        pass

    def _getParser(self):
        wsList     = AlphanumericWhiteSpaceList();
        normalizer = LowerCaseNormalizer();
        tokenizer  = Tokenizer(wsList, normalizer);
        outputDir  = path.dirname(path.realpath(__file__)) + path.sep + 'ParserTestData' + path.sep;
        partitions = ['d','lm','r','t'];
        partTable  = PartitionTable(partitions);
        stopWords  = StopWordList();
        stemmer    = StemmingWrapper();
        parser     = Parser(tokenizer, outputDir, stopWords, stemmer, partTable);
        return parser;

    def _getDocumentCollection(self):
        docCollDir         = path.dirname(path.realpath(__file__)) + path.sep + 'ParserTestData' + path.sep + 'documents.txt';
        docCollection = VirtualDocumentCollection(docCollDir);
        return docCollection;

    def test_parse(self):
        parser        = self._getParser();
        docCollection = self._getDocumentCollection();
        parser.parse(docCollection);


if __name__ == '__main__':
    unittest.main()