import unittest
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.abspath(path.join(__file__, "..", "..")))

from src.StopWordList import StopWordList
from src.Testing import *

class StopWordListTest(unittest.TestCase):
    def test___init__(self):
        obj = StopWordList()

    def dataProvider_isWhitespace(self):
        return [
            [ 'the', True ],
            [ 'is',  True ],
            [ 'at',  True ],
            [ 'of',  True ],
            [ 'on',  True ],
            [ 'and', True ],
            [ 'no',  False],
            [ 'to',  False],
            [ 'in',  False],
            [ 'I',   False]
        ]

    @dataProvider(dataProvider_isWhitespace)
    def test_isWhitespace(self, char, expected):
        anws   = StopWordList();
        result = anws.isStopWord(char);
        self.assertEqual(result, expected);

if __name__ == '__main__':
    unittest.main()