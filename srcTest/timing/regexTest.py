import unittest
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.abspath(path.join(__file__, "..", "..", "..")))

from src.timing.regex import regex
import random;

class regexTest(unittest.TestCase):
    _nbrLines = 10000000;
    _nbrTerms = 200000;
    _nbrDocs  = 400000;
    _nbrPos   = 10000;
    _lines    = None;

    def test___init__(self):
        obj = regex()

    def _getLines(self):
        if self._lines is None:
            result = "";
            for n in xrange(1,self._nbrLines):
                result += str(int(random.random() * self._nbrTerms)) + ',' + str(int(random.random() * self._nbrDocs)) + ',' + str(int(random.random() * self._nbrPos)) + "\n";
            self._lines = result;
        return self._lines;

    # def test_regexLineSplit(self):
    #     testSuite = {'output':True, 'lines': self._getLines(),'nbrLines':self._nbrLines};

    #     obj = regex();
    #     obj.regexLineSplit(testSuite);

    # def test_stringIOLineSplit(self):
    #     testSuite = {'output':True, 'lines': self._getLines(),'nbrLines':self._nbrLines};

    #     obj = regex();
    #     obj.stringIOLineSplit(testSuite);

    # def test_split(self):
    #     testSuite = {'output':True, 'lines': self._getLines(),'nbrLines':self._nbrLines};

    #     obj = regex();
    #     obj.split(testSuite);

    def test_array_access_test(self):
        testSuite = {'output':True,'nbrLines':self._nbrLines};

        obj = regex();
        obj.arrayRead(testSuite);


if __name__ == '__main__':
    unittest.main()