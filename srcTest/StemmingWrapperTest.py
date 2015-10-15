import unittest
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.abspath(path.join(__file__, "..", "..")))

from src.StemmingWrapper import StemmingWrapper

class StemmingWrapperTest(unittest.TestCase):
    def test___init__(self):
        stemmer = StemmingWrapper();

    def test_stem(self):
        stemmer = StemmingWrapper();
        token   = "cars";
        result  = stemmer.stem(token);
        self.assertEqual(result, 'car');


if __name__ == '__main__':
    unittest.main()