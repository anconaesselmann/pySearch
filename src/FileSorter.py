"""
Sorts the content of a file by reading lines into memory to be sorted, creating intermediary files,
that then get merged together.

@author Axel Ancona Esselmann
"""
import os,io;
from FileMerger import FileMerger;
import shutil

class FileSorter():
    def __init__(self, sortingAlgorythm, nbrInMemoryLines = 1000, deleteIntermediary = True):
        self._sortingAlgorythm   = sortingAlgorythm;
        self._nbrInMemoryLines   = nbrInMemoryLines;
        self._fileMerger         = FileMerger();
        self._deleteIntermediary = deleteIntermediary;

    def sort(self, fileName):
        fileHandler = io.open(fileName, 'r');
        self._tempDir = os.path.dirname(fileName) + os.path.sep + 'temp' + os.path.sep;
        if not os.path.exists(self._tempDir): os.makedirs(self._tempDir)
        done         = False;
        nbrTempFiles = 0;
        tempFiles    = [];
        # create intermediary sorted files
        while not done:
            # read lines into memory
            lines = [];
            for i in xrange(0, self._nbrInMemoryLines):
                line = fileHandler.readline();
                if not line:
                    done = True;
                    break;
                lines.append(line.strip());
            if done and len(lines) == 0: break;
            # sort lines in memory
            self._sortingAlgorythm.sort(lines);
            # write lines to file
            nbrTempFiles += 1;
            tempFileName = self._tempDir + str(nbrTempFiles) + '.txt';
            tempFiles.append(tempFileName);
            tempFile = io.open(tempFileName, 'wb');
            for i in xrange(0,len(lines)):
                string = lines[i] + '\n';
                tempFile.write(string);
            tempFile.close();
        # merge intermediary files and cleanup
        fileHandler.close();
        self._fileMerger.merge(tempFiles, fileName);
        if self._deleteIntermediary: shutil.rmtree(self._tempDir);