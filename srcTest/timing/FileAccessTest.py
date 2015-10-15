import unittest
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.abspath(path.join(__file__, "..", "..", "..")))

from src.timing.FileAccess import FileAccess;
import src.timing.Timing;
from src.FileBlock import FileBlock;



class FileAccessTest(unittest.TestCase):
    _dir             = path.dirname(path.realpath(__file__)) + path.sep + 'FileAccessTestData' + path.sep;
    _bufferSize      = 100;
    _regenerateFiles = False;
    _nbrFiles        = 10000;
    _output          = True;
    _shuffledIdArray  = None;
    _exponentiallyDistrArray = None;

    def test_description(self):
        obj = FileAccess();
        obj.description(self._output);

    def _generateIndividualFiles(self, testSuite):
        randText        = RandomText();
        files           = [];
        indivDynamicDir = testSuite['dir'] + ".individualFilesDynamic" + path.sep;
        for n in xrange(0,testSuite['nbrFiles']):
            rf = RandomFile(indivDynamicDir, randText);
            rf.setExtension(".txt");
            rf.create();
        return files;

    def _generateBlockFiles(self, testSuite):
        fb = FileBlock(
            testSuite['blockSize'],
            testSuite['bufferSize'],
            testSuite['blockFilesDir'],
            testSuite['tableFileName'],
        );
        for n in xrange(0, testSuite["nbrFiles"]):
            fileName  = testSuite['sourceFilesDir'] + str(n) + '.txt';
            currentFH = io.open(fileName, 'r');
            registry  = fb.write(n, currentFH);
        return fb, registry;
    def _getShuffledIdArray(self):
        if FileAccessTest._shuffledIdArray is None:
            fileIds = [];
            for i in xrange(0,self._nbrFiles):
                fileIds.append(i);
            shuffle(fileIds);
            FileAccessTest._shuffledIdArray = fileIds;
        return FileAccessTest._shuffledIdArray;

    def _getExponentiallyDistributedArray(self):
        fileIds = [];
        lambd = 1;
        for i in xrange(0,self._nbrFiles):
            var = expovariate(lambd);
            print var;
            # self._exponentiallyDistrArray.append();

    # def test_individualFiles(self):
    #     testSuite = {
    #         'nbrFiles': self._nbrFiles,
    #         'bufferSize':self._bufferSize,
    #         'dir':self._dir,
    #         'extension':'.txt',
    #         'output': self._output,
    #         'shuffledIdArray': self._getShuffledIdArray()
    #     };
    #     if self._regenerateFiles: self._generateIndividualFiles(testSuite);
    #     fa = FileAccess();
    #     fa.individualFiles(testSuite);

    def test_blockFiles(self):
        sourceFilesDir = self._dir + ".individualFilesDynamic" + path.sep;
        blockFilesDir  = self._dir + '.blockFilesDynamic' + path.sep;
        tableFileName  = self._dir + 'table.txt';
        testSuite      = {
            'blockSize':10000000,
            'bufferSize':1000 ,
            'nbrFiles': self._nbrFiles,
            'sourceFilesDir':sourceFilesDir,
            'blockFilesDir':blockFilesDir,
            'tableFileName':tableFileName,
            'output': self._output,
            'shuffledIdArray': self._getShuffledIdArray()
        };
        if self._regenerateFiles: fileBocks, registry = self._generateBlockFiles(testSuite);

        fa = FileAccess();
        fa.blockFiles(testSuite);

        self._getExponentiallyDistributedArray();


if __name__ == '__main__':
    unittest.main()