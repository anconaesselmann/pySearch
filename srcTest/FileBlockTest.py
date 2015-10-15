import unittest
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.abspath(path.join(__file__, "..", "..")))

from src.FileBlock import FileBlock

class DummyClass():
    def setA(self, var):
        self._var = var;

    def setBC(self, var1, var2):
        self._b = var1;
        self._c = var2;

    def sayHi(self):
        return self._var + self._b + self._c;

class FileBlockTest(unittest.TestCase):

    def _generateIndividualFiles(self, testSuite):
        randText        = RandomText();
        files           = [];
        indivDynamicDir = testSuite['dir'] + "individualFilesDynamic" + path.sep;
        for n in xrange(0,testSuite['nbrFiles']):
            rf = RandomFile(indivDynamicDir, randText);
            rf.setEnding(".txt");
            rf.create();
            files.append(rf);
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

    def test_blocks(self):
        dir = path.dirname(path.realpath(__file__)) + path.sep + 'FileBlockTestData' + path.sep;
        sourceFilesDir = dir + "individualFilesDynamic" + path.sep;
        blockFilesDir  = dir + 'blockFilesDynamic' + path.sep;
        tableFileName  = dir + 'table.txt';
        testSuite      = {'blockSize':951, 'bufferSize':80 , 'nbrFiles': 10, 'sourceFilesDir':sourceFilesDir, 'blockFilesDir':blockFilesDir, 'tableFileName':tableFileName};
        fileBlocks, registry = self._generateBlockFiles(testSuite);
        testSuite['nbrBlockFiles'] = fileBlocks.blockCount();

        id            = 1;
        record        = fileBlocks.getRecord(id);
        recordHandler = fileBlocks.open(record);
        string1       = '';
        buffer        = recordHandler.read(11);
        while buffer:
            string1 += buffer;
            buffer = recordHandler.read(11);

        indivFileName    = path.dirname(path.realpath(__file__)) + path.sep + 'FileBlockTestData' + path.sep + 'individualFilesDynamic' + path.sep + '1.txt';
        indivFileHandler = io.open(indivFileName, 'r');
        string2          = indivFileHandler.read(3467);

        self.assertEqual(string1, string2);
        self.assertEqual(len(string1), 3467);

    def test_loadRegistry(self):
        dir = path.dirname(path.realpath(__file__)) + path.sep + 'FileBlockTestData' + path.sep;
        sourceFilesDir = dir + "individualFilesDynamic" + path.sep;
        blockFilesDir  = dir + 'blockFilesDynamic' + path.sep;
        tableFileName  = dir + 'table.txt';
        testSuite      = {'blockSize':951, 'bufferSize':80 , 'nbrFiles': 10, 'sourceFilesDir':sourceFilesDir, 'blockFilesDir':blockFilesDir, 'tableFileName':tableFileName};
        fb = FileBlock(
            testSuite['blockSize'],
            testSuite['bufferSize'],
            testSuite['blockFilesDir'],
            testSuite['tableFileName'],
        );
        fb.loadRegistry();
        recordHandler    = fb.open(1);
        indivFileName    = path.dirname(path.realpath(__file__)) + path.sep + 'FileBlockTestData' + path.sep + 'individualFilesDynamic' + path.sep + '1.txt';
        indivFileHandler = io.open(indivFileName, 'r');
        bufferLen        = 10;
        buffer1          = recordHandler.read(bufferLen);
        buffer2          = indivFileHandler.read(bufferLen);
        self.assertEqual(buffer1, buffer2);
        self.assertEqual(len(buffer1), bufferLen);

    def test_readObject(self):
        dir = path.dirname(path.realpath(__file__)) + path.sep + 'FileBlockTestData' + path.sep;
        sourceFilesDir = dir + "individualFilesDynamic" + path.sep;
        blockFilesDir  = dir + 'blockFilesDynamic' + path.sep;
        tableFileName  = dir + 'table.txt';
        testSuite      = {'blockSize':951, 'bufferSize':80 , 'nbrFiles': 10, 'sourceFilesDir':sourceFilesDir, 'blockFilesDir':blockFilesDir, 'tableFileName':tableFileName};
        fb = FileBlock(
            testSuite['blockSize'],
            testSuite['bufferSize'],
            testSuite['blockFilesDir'],
            testSuite['tableFileName'],
        );
        fb.loadRegistry();
        recordHandler = fb.open(1);

        string = "343423,4325,22\n";


        compiledExpressionNamespaceAndClass = re.compile(r"""
            (?P<termId>.*),
            (?P<docId>.*),
            (?P<position>.*)
        """, re.S|re.X)


        match = re.match(compiledExpressionNamespaceAndClass, string)
        print int(match.group('termId'));
        print int(match.group('docId'));
        print int(match.group('position'));
        # if match:
        #     return match.group("NameSpace") + "\\", match.group("ClassName")

        # readMap

        # mapping = {''}
        # o = FileBlock.FileBlockRecord()

        # t = recordHandler.readObject(o);

        # print t.id;
        # t.out('works!!!!!!!!');


if __name__ == '__main__':
    unittest.main()