import unittest
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.abspath(path.join(__file__, "..", "..")))

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

class IndexerTest(unittest.TestCase):
    def _getParser(self):
        wsList     = AlphanumericWhiteSpaceList();
        normalizer = LowerCaseNormalizer();
        tokenizer  = Tokenizer(wsList, normalizer);
        outputDir  = path.dirname(path.realpath(__file__)) + path.sep + 'IndexerTestData' + path.sep;
        partitions = [];
        partTable  = PartitionTable(partitions);
        stopWords  = StopWordList();
        stemmer    = StemmingWrapper();
        parser     = Parser(tokenizer, outputDir, stopWords, stemmer, partTable);
        return parser;

    def _getInverter(self):
        outputDir  = path.dirname(path.realpath(__file__)) + path.sep + 'IndexerTestData' + path.sep + 'invTemp' + path.sep;
        stemmer    = StemmingWrapper();
        sortAlgym  = QuickSort();
        fileSorter = FileSorter(sortAlgym, 1000 , False);
        fileMerger = FileMerger();
        inverter   = Inverter(outputDir, stemmer, fileSorter, fileMerger);
        return inverter;

    def test_index(self):
        parser     = self._getParser();
        inputDirs  = [];
        inverter   = self._getInverter();
        blockFilesDir = path.dirname(path.realpath(__file__)) + path.sep + 'IndexerTestData' + path.sep + 'index' + path.sep;
        blockSize = 1000;
        bufferSize = 100;
        tableFileName = path.dirname(path.realpath(__file__)) + path.sep + 'IndexerTestData' + path.sep + 'index' + path.sep + 'indexTable.txt';
        dictionaryFile = path.dirname(path.realpath(__file__)) + path.sep + 'IndexerTestData' + path.sep + 'index' + path.sep + 'dictionary.txt';

        indexFileBlock = FileBlock(
            blockSize,
            bufferSize,
            blockFilesDir,
            tableFileName,
        );
        indexer    = Indexer(parser, inverter, indexFileBlock, dictionaryFile);
        fileName   = path.dirname(path.realpath(__file__)) + path.sep + 'IndexerTestData' + path.sep + 'documents.txt';
        docCollect = VirtualDocumentCollection(fileName);

        indexer.index(docCollect);



if __name__ == '__main__':
    unittest.main()