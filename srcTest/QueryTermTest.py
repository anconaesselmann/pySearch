import unittest
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.abspath(path.join(__file__, "..", "..")))

from src.QueryTerm import QueryTerm

class QueryTermTest(unittest.TestCase):
	def test___init__(self):
		obj = QueryTerm()

	

if __name__ == '__main__':
    unittest.main()