import unittest
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.abspath(path.join(__file__, "..", "..")))

from src.Random import Random

class RandomTest(unittest.TestCase):
	def test___init__(self):
		obj = Random()

	

if __name__ == '__main__':
    unittest.main()