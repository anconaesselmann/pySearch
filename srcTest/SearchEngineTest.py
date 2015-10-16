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

class SearchEngineTest(unittest.TestCase):
    blockSize       = 10000;
    bufferSize      = 100;
    dictionaryDir   = path.dirname(path.realpath(__file__)) + path.sep + 'SearchEngineTestData' + path.sep + 'index' + path.sep + 'dictionary.txt';
    blockFilesDir   = path.dirname(path.realpath(__file__)) + path.sep + 'SearchEngineTestData' + path.sep + 'index' + path.sep;
    tableFileName   = path.dirname(path.realpath(__file__)) + path.sep + 'SearchEngineTestData' + path.sep + 'index' + path.sep + 'indexTable.txt';
    dictionaryFile  = path.dirname(path.realpath(__file__)) + path.sep + 'SearchEngineTestData' + path.sep + 'index' + path.sep + 'dictionary.txt';
    docIds          = path.dirname(path.realpath(__file__)) + path.sep + 'SearchEngineTestData' + path.sep + 'invTemp' + path.sep + 'inverter_1_documentIds.txt';
    docCollFileName = path.dirname(path.realpath(__file__)) + path.sep + 'SearchEngineTestData' + path.sep + 'documents.txt';


    def _getParser(self):
        wsList     = AlphanumericWhiteSpaceList();
        normalizer = LowerCaseNormalizer();
        tokenizer  = Tokenizer(wsList, normalizer);
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

    def test_reloadDictionary(self):
        self._create_index();
        indexFileBlock = self._getFile();

        stemmer    = StemmingWrapper();
        stopWords  = StopWordList();
        queryTokenizer = QueryTokenizer();

        se = SearchEngine(self.dictionaryDir, indexFileBlock, stemmer, stopWords, self.docIds, queryTokenizer);


        # print "search result for 'nexus like love happy': "
        # result = se.search("nexus like love happy");
        # # self.assertEqual(result, []);
        # print result;
        # print "search result for 'asus repair': "
        # result = se.search("asus repair");
        # # self.assertEqual(result, []);
        # print result;
        # print "search result for '0(touch screen) fix repair': "
        # result = se.search("0(touch screen) fix repair");
        # # self.assertEqual(result, []);
        # print result;
        print "search result for '1(great tablet) 2(tablet fast)': "
        result = se.search("1(great tablet) temp bla 2(tablet fast) fu");
        # self.assertEqual(result, []);
        print result;
        # print "search result for 'tablet': "
        # result = se.search("tablet");
        # # self.assertEqual(result, []);
        # print result;




        # print "\nsearch result for 'asus AND google': "
        # result = se.search("asus AND google");
        # self.assertEqual(result, [1,8]);
        # print result;

        # print "search result for 'screen AND bad': "
        # result = se.search("screen AND bad");
        # self.assertEqual(result, [3]);
        # print result;

        # print "search result for 'great AND tablet': "
        # result = se.search("great AND tablet");
        # self.assertEqual(result, [2,3,6]);
        # print result;


if __name__ == '__main__':
    unittest.main()