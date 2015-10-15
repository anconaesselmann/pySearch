import unittest
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.abspath(path.join(__file__, "..", "..")))

from src.AlphanumericWhiteSpaceList import AlphanumericWhiteSpaceList
from src.Testing import *

class AlphanumericWhiteSpaceListTest(unittest.TestCase):
    def test___init__(self):
        obj = AlphanumericWhiteSpaceList();

    def dataProvider_isWhitespace(self):
        return [
            [ 'a', False],
            [ 'Z', False],
            [ '8', False],
            [ '_', False],
            [ '*', True],
            [ '+', True],
            [ ' ', True],
            [ '.', True]
        ]

    @dataProvider(dataProvider_isWhitespace)
    def test_isWhitespace(self, char, expected):
        anws   = AlphanumericWhiteSpaceList();
        result = anws.isWhitespace(char);
        self.assertEqual(result, expected);

if __name__ == '__main__':
    unittest.main()