import unittest
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.abspath(path.join(__file__, "..", "..")))

from src.SearchEngine import SearchEngine
from src.FileBlock import FileBlock;
from src.StemmingWrapper import StemmingWrapper;
from src.StopWordList import StopWordList;

from src.AlphanumericWhiteSpaceList import AlphanumericWhiteSpaceList;
from src.FileMerger import FileMerger
from src.FileSorter import FileSorter;
from src.Indexer import Indexer
from src.Inverter import Inverter;
from src.LowerCaseNormalizer import LowerCaseNormalizer;
from src.Parser import Parser
from src.PartitionTable import PartitionTable;
from src.sorting.QuickSort import QuickSort;
from src.StemmingWrapper import StemmingWrapper;
from src.StopWordList import StopWordList;
from src.Tokenizer import Tokenizer;
from src.VirtualDocumentCollection import VirtualDocumentCollection;
from src.FileBlock import FileBlock;
from src.QueryTokenizer import QueryTokenizer;

class SearchEngineTest(unittest.TestCase):
    blockSize       = 10000;
    bufferSize      = 100;
    dictionaryDir   = path.dirname(path.realpath(__file__)) + path.sep + 'SearchEngineTestData' + path.sep + 'index' + path.sep + 'dictionary.txt';
    blockFilesDir   = path.dirname(path.realpath(__file__)) + path.sep + 'SearchEngineTestData' + path.sep + 'index' + path.sep;
    tableFileName   = path.dirname(path.realpath(__file__)) + path.sep + 'SearchEngineTestData' + path.sep + 'index' + path.sep + 'indexTable.txt';
    dictionaryFile  = path.dirname(path.realpath(__file__)) + path.sep + 'SearchEngineTestData' + path.sep + 'index' + path.sep + 'dictionary.txt';
    docIds          = path.dirname(path.realpath(__file__)) + path.sep + 'SearchEngineTestData' + path.sep + 'invTemp' + path.sep + 'inverter_1_documentIds.txt';
    docCollFileName = path.dirname(path.realpath(__file__)) + path.sep + 'SearchEngineTestData' + path.sep + 'documents.txt';

    def _getTokenizer(self):
        wsList     = AlphanumericWhiteSpaceList();
        normalizer = LowerCaseNormalizer();
        tokenizer  = Tokenizer(wsList, normalizer);
        return tokenizer;

    def _getParser(self):
        tokenizer  = self._getTokenizer();
        outputDir  = path.dirname(path.realpath(__file__)) + path.sep + 'SearchEngineTestData' + path.sep + 'invTemp' + path.sep;
        partitions = [];
        partTable  = PartitionTable(partitions);
        stopWords  = StopWordList();
        stemmer    = StemmingWrapper();
        parser     = Parser(tokenizer, outputDir, stopWords, stemmer, partTable);
        return parser;

    def _getInverter(self):
        outputDir  = path.dirname(path.realpath(__file__)) + path.sep + 'SearchEngineTestData' + path.sep + 'invTemp' + path.sep;
        stemmer    = StemmingWrapper();
        sortAlgym  = QuickSort();
        fileSorter = FileSorter(sortAlgym, 1000000 , False);
        fileMerger = FileMerger();
        inverter   = Inverter(outputDir, stemmer, fileSorter, fileMerger);
        return inverter;
    def _getFile(self):
        indexFileBlock = FileBlock(
            self.blockSize,
            self.bufferSize,
            self.blockFilesDir,
            self.tableFileName,
        );
        indexFileBlock.loadRegistry();
        return indexFileBlock;
    def _create_index(self):
        parser     = self._getParser();
        inputDirs  = [];
        inverter   = self._getInverter();
        indexFileBlock = self._getFile();
        indexer    = Indexer(parser, inverter, indexFileBlock, self.dictionaryFile);
        docCollect = VirtualDocumentCollection(self.docCollFileName);
        indexer.index(docCollect);
        return docCollect;

    def test_reloadDictionary(self):
        docCollect     = self._create_index();
        indexFileBlock = self._getFile();
        tokenizer      = self._getTokenizer();

        stemmer    = StemmingWrapper();
        stopWords  = StopWordList();
        queryTokenizer = QueryTokenizer();

        for i in xrange(1,6):
            se = SearchEngine(self.dictionaryDir, indexFileBlock, stemmer, stopWords, self.docIds, queryTokenizer);
            se.setDocCollect(docCollect);
            se.setTokenizer(tokenizer);
            queryExpansionParameter = i;
            se.search("battery", queryExpansionParameter);
            se.search("screen", queryExpansionParameter);
            se.search("speed", queryExpansionParameter);






if __name__ == '__main__':
    unittest.main()