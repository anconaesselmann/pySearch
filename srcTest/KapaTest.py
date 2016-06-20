import unittest
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.abspath(path.join(__file__, "..", "..")))

from src.Kapa import Kapa

class KapaTest(unittest.TestCase):
    def test___init__(self):
        obj = Kapa();
        print obj.calculate("/Dropbox/python/SFSU/849/Homework4_AxelAnconaEsselmann/src/rj/axel-qrels.txt", "/Dropbox/python/SFSU/849/Homework4_AxelAnconaEsselmann/src/rj/beasely-qrels.txt");
        print obj.calculate("/Dropbox/python/SFSU/849/Homework4_AxelAnconaEsselmann/src/rj/axel-qrels.txt", "/Dropbox/python/SFSU/849/Homework4_AxelAnconaEsselmann/src/rj/Chuang-qrels.txt");
        print obj.calculate("/Dropbox/python/SFSU/849/Homework4_AxelAnconaEsselmann/src/rj/axel-qrels.txt", "/Dropbox/python/SFSU/849/Homework4_AxelAnconaEsselmann/src/rj/kkatipally-qrels.txt");
        print obj.calculate("/Dropbox/python/SFSU/849/Homework4_AxelAnconaEsselmann/src/rj/axel-qrels.txt", "/Dropbox/python/SFSU/849/Homework4_AxelAnconaEsselmann/src/rj/ng-qrels.txt");
        print obj.calculate("/Dropbox/python/SFSU/849/Homework4_AxelAnconaEsselmann/src/rj/axel-qrels.txt", "/Dropbox/python/SFSU/849/Homework4_AxelAnconaEsselmann/src/rj/saylor-qrels-2.txt");



if __name__ == '__main__':
    unittest.main()