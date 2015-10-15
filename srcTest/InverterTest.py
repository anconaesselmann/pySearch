import unittest
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.abspath(path.join(__file__, "..", "..")))

from src.Inverter import Inverter;
from src.StemmingWrapper import StemmingWrapper;
from src.FileSorter import FileSorter;
from src.FileMerger import FileMerger
from src.sorting.QuickSort import QuickSort;

class InverterTest(unittest.TestCase):
    def _getInverter(self):
        outputDir  = path.dirname(path.realpath(__file__)) + path.sep + 'InverterTestData' + path.sep;
        stemmer    = StemmingWrapper();
        sortAlgym  = QuickSort();
        fileSorter = FileSorter(sortAlgym, 10);
        fileMerger = FileMerger();
        inverter   = Inverter(outputDir, stemmer, fileSorter, fileMerger);
        return inverter;

    def test_create(self):
        fileDir1    = path.dirname(path.realpath(__file__)) + path.sep + 'InverterTestData' + path.sep + '1.txt';
        fileHandler = io.open(fileDir1, 'wb');
        fileHandler.write("muffler,doc_4,458\nnonadventitious,doc_1,155\nrook,doc_2,96\nunbloused,doc_3,347\nunbloused,doc_5,449\ncosmogony,doc_4,350\ndecimal,doc_5,410\nenterozoon,doc_3,4\ninteresting,doc_5,237\nintermatting,doc_2,397\nkinesiology,doc_3,257\nmuffler,doc_5,18\nnonadventitious,doc_4,238\nrook,doc_4,200\nunbloused,doc_5,287\ncosmogony,doc_3,336\ndecimal,doc_3,67\nenterozoon,doc_3,56\ninteresting,doc_3,496\nintermatting,doc_5,340\nkinesiology,doc_4,208\nmuffler,doc_4,457\nnonadventitious,doc_1,71\nrook,doc_2,15\nunbloused,doc_3,448\ncosmogony,doc_1,34\ndecimal,doc_3,151\nenterozoon,doc_3,9\nrook,doc_5,395\nunbloused,doc_5,117\ncosmogony,doc_5,140\ndecimal,doc_1,451\nenterozoon,doc_4,418\n");
        fileHandler.close();

        fileDir2    = path.dirname(path.realpath(__file__)) + path.sep + 'InverterTestData' + path.sep + '2.txt';
        fileHandler = io.open(fileDir2, 'wb');
        fileHandler.write("ajo,doc_3,390\nbootblack,doc_2,76\nepicedium,doc_5,325\nfulminate,doc_4,249\ngeisha,doc_5,380\nmunt,doc_2,229\nnonmitigative,doc_4,147\nremorse,doc_5,277\nrook,doc_3,61\nunbloused,doc_5,112\ncosmogony,doc_4,45\ndecimal,doc_5,35\nenterozoon,doc_3,444\ninteresting,doc_5,490\nintermatting,doc_2,159\nkinesiology,doc_3,370\nmuffler,doc_5,354\nnonadventitious,doc_4,384\nrook,doc_4,75\nunbloused,doc_5,164\ncosmogony,doc_3,446\ndecimal,doc_3,124\nenterozoon,doc_3,105\ninteresting,doc_3,360\nintermatting,doc_5,358\nkinesiology,doc_4,16\n");
        fileHandler.close();

        inputDirs = [ fileDir1, fileDir2 ];
        inverter  = self._getInverter();
        inverter.create(inputDirs);

if __name__ == '__main__':
    unittest.main()