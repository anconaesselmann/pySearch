import unittest
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.abspath(path.join(__file__, "..", "..")))

from src.PartitionTable import PartitionTable
from src.Testing import *

class PartitionTableTest(unittest.TestCase):
    def test___init__(self):
        partitions = ['d','lm','r','t'];
        obj = PartitionTable(partitions);

    def dataProvider_getPartitionId(self):
        return [
            [ 'apple', 0 ],
            [ 'light', 1 ],
            [ 'long', 2 ],
            [ 'query', 2 ],
            [ 'rat', 3 ],
            [ 'stamp', 3 ],
            [ 'time', 4 ],
            [ 'union', 4 ]
        ]

    @dataProvider(dataProvider_getPartitionId)
    def test_getPartitionId(self, token, expected):
        # Given a partition table
        partitions = ['d','lm','r','t'];
        partTable = PartitionTable(partitions);
        # When getPartitionId is called
        result = partTable.getPartitionId(token)
        # Then a partition id from 0 to nbr of partitions - 1 is returned
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()