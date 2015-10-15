"""
Inverter takes partitions created by parser and creates precursor files to an inverted index to be used by Indexer.

@author Axel Ancona Esselmann
"""
import io;
from os import path;
from IndexList import IndexList;

class Inverter():
    def __init__(self, outputDir, stemmer, fileSorter, fileMerger, inverterId = 'inverter_1'):
        self._indexExtension      = '.txt';
        self._stemmer             = stemmer;
        self._mergedFileName      = outputDir + inverterId + '_merged'      + self._indexExtension;
        self._collapsedFileName   = outputDir + inverterId + '_collapsed'   + self._indexExtension;
        self._documentIdsFileName = outputDir + inverterId + '_documentIds' + self._indexExtension;
        self._fileSorter          = fileSorter;
        self._fileMerger          = fileMerger;
        self._documentIds         = {};
        self._docIdCounter        = 0;

        docIdFH = io.open(self._documentIdsFileName,   'wb');
        docIdFH.close();
        collapsedFH = io.open(self._collapsedFileName, 'wb');
        collapsedFH.close();

    def startDocIdsAt(self, docId):
        set._docIdCounter = docId;

    def _generateDocId(self, docName):
        if docName in self._documentIds: result = self._documentIds[docName];
        else:
            self._documentIds[docName] = self._docIdCounter;
            docIdFH = io.open(self._documentIdsFileName, 'ab');
            docIdFH.write(str(self._docIdCounter) + ',' + docName + '\n');
            docIdFH.close();

            self._docIdCounter += 1;
            result = self._docIdCounter - 1;
        return result;

    def create(self, inputDirs):
        self._inputDirs = inputDirs;
        for i in xrange(0, len(self._inputDirs)):
            self._fileSorter.sort(self._inputDirs[i]);
        self._fileMerger.merge(self._inputDirs, self._mergedFileName);

        mergedFH     = io.open(self._mergedFileName,      'r');
        collapsedFH  = io.open(self._collapsedFileName,   'a');

        line         = mergedFH.readline();
        index        = IndexList();
        prevTerm     = None;
        while line:
            parts = line.split(',');
            index.insert(parts[0], parts[1], int(parts[2]));
            line  = mergedFH.readline();
        for term in index:
            termName      = term.term;
            termFrequency = term.count;
            termDocs      = term.docs;
            docNode       = termDocs.next;
            termString    = termName + ':' + str(termFrequency)
            while docNode is not None:
                docName           = docNode.value.doc;
                docId             = str(self._generateDocId(docName));
                documentFrequency = docNode.value.count;
                docString         =  '|' + docId + ':' + str(documentFrequency) + ';';
                lineNode          = docNode.value.lines.next;
                lineString        = '';
                while lineNode is not None:
                    line = lineNode.value;
                    if len(lineString) > 0: lineString += ',';
                    lineString += str(line.line);
                    lineNode    = lineNode.next;
                docString  += lineString;
                termString += docString;
                docNode = docNode.next;
            # print termString;
            collapsedFH.write(termString + '\n');
        collapsedFH.close();

    def getCollapsedOutputFileDir(self):
        return self._collapsedFileName;


