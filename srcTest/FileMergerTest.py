import unittest
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.abspath(path.join(__file__, "..", "..")))

from src.FileMerger import FileMerger
import io;

class FileMergerTest(unittest.TestCase):
    def test_merge(self):
        inputDirs = [
            path.dirname(path.realpath(__file__)) + path.sep + 'FileMergerTestData' + path.sep + '1.txt',
            path.dirname(path.realpath(__file__)) + path.sep + 'FileMergerTestData' + path.sep + '2.txt',
            path.dirname(path.realpath(__file__)) + path.sep + 'FileMergerTestData' + path.sep + '3.txt',
            path.dirname(path.realpath(__file__)) + path.sep + 'FileMergerTestData' + path.sep + '4.txt',
            path.dirname(path.realpath(__file__)) + path.sep + 'FileMergerTestData' + path.sep + '5.txt',
            path.dirname(path.realpath(__file__)) + path.sep + 'FileMergerTestData' + path.sep + '6.txt',
            path.dirname(path.realpath(__file__)) + path.sep + 'FileMergerTestData' + path.sep + '7.txt',
            path.dirname(path.realpath(__file__)) + path.sep + 'FileMergerTestData' + path.sep + '8.txt',
            path.dirname(path.realpath(__file__)) + path.sep + 'FileMergerTestData' + path.sep + '9.txt',
            path.dirname(path.realpath(__file__)) + path.sep + 'FileMergerTestData' + path.sep + '10.txt'
        ];
        outputDir   = path.dirname(path.realpath(__file__)) + path.sep + 'FileMergerTestData' + path.sep + 'output.txt';
        expectedDir = path.dirname(path.realpath(__file__)) + path.sep + 'FileMergerTestData' + path.sep + 'expected.txt';
        fileMerger  = FileMerger();
        fileMerger.merge(inputDirs, outputDir);

        resultHandle   = io.open(outputDir, 'r');
        result         = resultHandle.read();
        expectedHandle = io.open(expectedDir, 'r');
        expected       = expectedHandle.read();

        self.assertEqual(expected, result)
        self.assertEqual(1017, len(result))

if __name__ == '__main__':
    unittest.main()