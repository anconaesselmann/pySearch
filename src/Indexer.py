"""
Indexer creates an inverted index and a dictionary for a document collection.

@author Axel Ancona Esselmann
"""
import StringIO, io;
class Indexer():
    def __init__(self, parser, inverter, indexStorage, dictionaryFile):
        self._parser = parser;
        self._inverter = inverter;
        self._indexStorage = indexStorage;
        self._dictionaryFile = dictionaryFile;

    def index(self, docCollect):
        self._parser.parse(docCollect);
        parserOutputDirs = self._parser.getOutputFileNames();
        self._inverter.create(parserOutputDirs);

        collapsedFileDir = self._inverter.getCollapsedOutputFileDir();
        collapsedFileHandler = io.open(collapsedFileDir, 'r');

        dictFH = io.open(self._dictionaryFile, 'wb');

        line = collapsedFileHandler.readline();
        i = -1;
        while line:
            i += 1;

            upBarParts    = line.split('|');
            termParts     = upBarParts[0].split(':');
            termName      = termParts[0];
            termFrequency = termParts[1];

            postingListFH = StringIO.StringIO()
            postingListFH.write(line);
            postingListFH.seek(0);
            self._indexStorage.write(str(i), postingListFH);

            line = collapsedFileHandler.readline();

            dictFH.write(termName + ',' + str(i) + '\n');

        dictFH.close();
