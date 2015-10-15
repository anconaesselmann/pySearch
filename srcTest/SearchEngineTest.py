import unittest
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.abspath(path.join(__file__, "..", "..")))

from src.SearchEngine import SearchEngine
from src.FileBlock import FileBlock;
from src.StemmingWrapper import StemmingWrapper;
from src.StopWordList import StopWordList;

class SearchEngineTest(unittest.TestCase):
    def test_reloadDictionary(self):
        dictionaryDir   =  path.dirname(path.realpath(__file__)) + path.sep + 'SearchEngineTestData' + path.sep + 'index' + path.sep + 'dictionary.txt';

        blockFilesDir = path.dirname(path.realpath(__file__)) + path.sep + 'SearchEngineTestData' + path.sep + 'index' + path.sep;
        blockSize = 1000;
        bufferSize = 100;
        tableFileName = path.dirname(path.realpath(__file__)) + path.sep + 'SearchEngineTestData' + path.sep + 'index' + path.sep + 'indexTable.txt';
        dictionaryFile = path.dirname(path.realpath(__file__)) + path.sep + 'SearchEngineTestData' + path.sep + 'index' + path.sep + 'dictionary.txt';
        docIds = path.dirname(path.realpath(__file__)) + path.sep + 'SearchEngineTestData' + path.sep + 'index' + path.sep + 'inverter_1_documentIds.txt';

        indexFileBlock = FileBlock(
            blockSize,
            bufferSize,
            blockFilesDir,
            tableFileName,
        );
        indexFileBlock.loadRegistry();

        stemmer    = StemmingWrapper();
        stopWords  = StopWordList();

        se = SearchEngine(dictionaryDir, indexFileBlock, stemmer, stopWords, docIds);

        # print se.getPostingList('for');

        print "\nsearch result for 'asus AND google': "
        result = se.search("asus AND google");
        print result;

        print "search result for 'screen AND bad': "
        result = se.search("screen AND bad");
        print result;

        print "search result for 'great AND tablet': "
        result = se.search("great AND tablet");
        print result;


if __name__ == '__main__':
    unittest.main()