import unittest
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.abspath(path.join(__file__, "..", "..")))

from src.LowerCaseNormalizer import LowerCaseNormalizer

class LowerCaseNormalizerTest(unittest.TestCase):
    def test___init__(self):
        normalizer = LowerCaseNormalizer()

    def test_normalize(self):
        # Given a token with upper and lower case characters
        normalizer = LowerCaseNormalizer();

        # When normalize is called
        result = normalizer.normalize('aTestString');

        # Then a token is returned with all lower case characters
        self.assertEqual('ateststring', result)


if __name__ == '__main__':
    unittest.main()