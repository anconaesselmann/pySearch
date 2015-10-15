import unittest
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.abspath(path.join(__file__, "..", "..")))

from src.LinkedList import LinkedList;
from src.Testing import *

class LinkedListTest(unittest.TestCase):
    def dataProvider_insert(self):
        return [
            [ # data set 1
                [8,3,8,6,1,4,5,9,2,8], None
            ],
        ]

    @dataProvider(dataProvider_insert)
    def test_insert(self, stringValues, expected):
        # Given
        ll = LinkedList()

        # When
        for i in xrange(0, len(stringValues)):
            ll.insert(stringValues[i]);

        result = ll.toString(',');
        # Then
        self.assertEqual('1,2,3,4,5,6,8,8,8,9', result);

    @dataProvider(dataProvider_insert)
    def test_getItem(self, stringValues, expected):
        # Given
        ll = LinkedList()

        # When
        for i in xrange(0, len(stringValues)):
            item = ll.getItem(stringValues[i]);
            ll.insertAtHead(stringValues[i]);


        result = ll.toString(',');
        # Then
        self.assertEqual('1,2,3,4,5,6,8,8,8,9', result);

    # @dataProvider(dataProvider_insert)
    # def test_insert(self, stringValues, expected):
    #     # Given
    #     ll = LinkedList()
    #     # When
    #     for i in xrange(0, len(stringValues)):
    #         ll.insert(stringValues[i]);

    #     for i in ll.next:
    #         # print type(item);
    #         return;
    #     # Then
    #     self.assertEqual('1,2,3,4,5,6,8,8,8,9', result);


if __name__ == '__main__':
    unittest.main()