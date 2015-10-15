import unittest
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.abspath(path.join(__file__, "..", "..")))

from src.IndexList import IndexList

class IndexListTest(unittest.TestCase):
	def test___init__(self):
		obj = IndexList()

if __name__ == '__main__':
    unittest.main()