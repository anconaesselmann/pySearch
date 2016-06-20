import io;
"""
@author Axel Ancona Esselmann
"""
class Kapa():
    def __init__(self):
        self._filePointerA = None;
        self._filePointerB = None;

    def calculate(self, fileNameA, fileNameB):
        self._initFiles(fileNameA, fileNameB);
        bothAgree = 0;
        bothDisagree = 0;
        aAgrees = 0;
        bAgrees = 0;
        elements = 0;
        a, b = self._getScore();
        while a is not None:
            elements += 1;
            if a & b: bothAgree += 1;
            elif (not a) & (not b): bothDisagree += 1;
            elif (not a) & b: bAgrees += 1;
            elif a & (not b): aAgrees += 1;
            a, b = self._getScore();

        p0 = (bothAgree + bothDisagree) / float(elements);
        pe = (
                (bothAgree + aAgrees) / float(elements) *
                (bothAgree + bAgrees) / float(elements)
            ) + (
                (1 - (bothAgree + aAgrees)) / float(elements) *
                (1 - (bothAgree + bAgrees)) / float(elements)
            );
        return 1 - ((1 - p0) / (1 - pe));

    def _initFiles(self, fileNameA, fileNameB):
        self._filePointerA = open(fileNameA,"rb");
        self._filePointerB = open(fileNameB,"rb");

    def _getScore(self):
        lineA = self._filePointerA.readline();
        if lineA == '': return None, None;
        partsA = lineA.split(" ");
        relevanceJudgementA = bool(int(partsA[3].strip()));
        lineB = self._filePointerB.readline();
        partsB = lineB.split(" ");
        relevanceJudgementB = bool(int(partsB[3].strip()));
        return relevanceJudgementA, relevanceJudgementB;

