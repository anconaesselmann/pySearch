"""
Merges two sorted files into one

@author Axel Ancona Esselmann
"""
import io;

class FileMerger():
    def merge(self, inputDirs, outputDir):
        # setup
        fh = io.open(outputDir, 'wb');
        self._inFileHandlers = [];
        self._currentLines   = [];
        for i in xrange(0,len(inputDirs)):
            self._inFileHandlers.append(io.open(inputDirs[i], 'r'));
            self._currentLines.append(self._inFileHandlers[i].readline());
        self._nbrUnsortedFiles = len(inputDirs);
        # merge
        while self._nbrUnsortedFiles > 0:
            hotLineNbr = hotFile = 0;
            for i in xrange(1,self._nbrUnsortedFiles):
                if self._currentLines[i] < self._currentLines[hotLineNbr]:
                    hotLineNbr = hotFile = i;
            fh.write(self._currentLines[hotLineNbr]);
            self._currentLines[hotFile] = self._inFileHandlers[hotFile].readline();
            self._removeEmptyFiles(hotFile);
        # release resources
        for i in xrange(0,len(inputDirs)):
            self._inFileHandlers[i].close();

    def _removeEmptyFiles(self, hotFile):
        if not self._currentLines[hotFile]:
            for j in xrange(hotFile,self._nbrUnsortedFiles - 1):
                self._currentLines[j] = self._currentLines[j + 1];
                self._inFileHandlers[j] = self._inFileHandlers[j + 1];
            self._nbrUnsortedFiles -= 1;

