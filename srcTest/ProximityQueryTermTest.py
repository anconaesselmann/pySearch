import unittest
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.abspath(path.join(__file__, "..", "..")))

from src.ProximityQueryTerm import ProximityQueryTerm

class ProximityQueryTermTest(unittest.TestCase):
	def test___init__(self):
		obj = ProximityQueryTerm()

	

if __name__ == '__main__':
    unittest.main()