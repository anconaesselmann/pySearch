import unittest
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.abspath(path.join(__file__, "..", "..")))
import io;

from src.FileSorter import FileSorter
from src.sorting.QuickSort import QuickSort;

class FileSorterTest(unittest.TestCase):
    def test_sort(self):
        fileDir     = path.dirname(path.realpath(__file__)) + path.sep + 'FileSorterTestData' + path.sep + '1.txt';
        fileHandler = io.open(fileDir, 'wb');
        fileHandler.write("nonmitigative\nunbloused\nmunt\najo\nbootblack\nfulminate\nrook\nepicedium\nremorse\ngeisha\nspirket\ndecimal\ninteresting\nnonadventitious\nunsuppressed\nkinesiology\nenterozoon\ncosmogony\nintermatting\nmuffler\nunsurmounted\nerlanger\nmarshland\nwired\nsubspecializing\nhesitantly\nfin\nkoku\nradiometry\nporphyritic\nbent\ngonangia\ncrestfish\ntriphthong\nnonecliptical\nactinoid\nwicked\ncystoscope\ndipolar\ncytozoic\netcetera\nloftier\nkapote\ngesturer\nbiblical\nerasable\ncorybantian\ncausativeness\nimparkation\nchongjin\ncollunarium\nsassoon\ncoaction\npupillage\nlorrain\ncompactification\nbaku\nraising\nprvert\nsanctifyingly\nuninterpleaded\nfelspar\nlullingly\nnonbranded\nlamoureux\nmetabolous\ndairywoman\nkennebec\nneuroblast\nnonrealizing\npreposition\ngrown\ncozing\nunmusical\nbehooving\nunsympathized\nradiotelephonic\ncharlot\ndenudate\nzidkijah\nneuropterous\nsterlingness\nuncomplaisant\nbaking\nunequivocal\nhousewifeliness\nlamaistic\ncalvinistical\ncir\nparental\nshreveport\nclydebank\nprebranchial\ninterhabitation\nninevite\nunslackening\nsummarized\nprecogitating\ncopy\norbicularity");
        fileHandler.close();
        sortingAlgorythm = QuickSort();
        nbrInMemoryLines = 10;

        fileSorter  = FileSorter(sortingAlgorythm, nbrInMemoryLines);
        fileSorter.sort(fileDir);
if __name__ == '__main__':
    unittest.main()