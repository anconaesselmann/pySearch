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
        self._documentTokenCountsTempFileName = outputDir + inverterId + '_docTokenCount_temp' + self._indexExtension;
        self._documentTokenCountsFileName = outputDir + inverterId + '_docTokenCount' + self._indexExtension;
        self._documentTotalDocCount = outputDir + inverterId + '_docTotalDocCount' + self._indexExtension;
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

    # document tokens have been stored with document names. The names have to be converted to ids.
    def _convertDocumentTokenCounts(self):
        docTokenCount_tempFH = io.open(self._documentTokenCountsTempFileName, 'rb');
        docTokenCountFH = io.open(self._documentTokenCountsFileName, 'wb');
        while True:
            line = docTokenCount_tempFH.readline()
            lineParts = line.rstrip().split(",")
            if not line: break
            newLine = str(self._generateDocId(lineParts[0])) + "," + lineParts[1] + "\n";
            docTokenCountFH.write(newLine);
        docTokenCount_tempFH.close();
        docTokenCountFH.close();

    def create(self, inputDirs):
        self._convertDocumentTokenCounts();
        self._inputDirs = inputDirs;
        for i in xrange(0, len(self._inputDirs)):
            self._fileSorter.sort(self._inputDirs[i]);
        self._fileMerger.merge(self._inputDirs, self._mergedFileName);

        mergedFH     = io.open(self._inputDirs[0],      'rb');
        collapsedFH  = io.open(self._collapsedFileName, 'wb');

        line         = mergedFH.readline();
        index        = IndexList();
        prevTerm     = None;
        while line:
            parts = line.split(',');
            lastInserted = index.insert(parts[0], parts[1], int(parts[2]));
            line  = mergedFH.readline();
            if prevTerm == parts[1]:
                lastInserted.count += -1;
            prevTerm = parts[1];
        index.reset();
        count = 0;
        for term in index:
            termName      = term.term;
            termFrequency = term.count;
            termString    = termName + ':' + str(termFrequency)
            term.reset();
            for doc in term:
                docId             = str(self._generateDocId(doc.doc));
                documentFrequency = doc.count;
                docString         =  '|' + docId + ':' + str(documentFrequency) + ';';
                lineString = '';
                doc.reset();
                for line in doc:
                    if len(lineString) > 0: lineString += ',';
                    lineString += str(line.line);
                docString  += lineString;
                termString += docString;
            collapsedFH.write(termString + '\n');
            # print termString
        docTokenCountFH = io.open(self._documentTotalDocCount, 'wb');
        docTokenCountFH.write(str(self._docIdCounter));
        docTokenCountFH.close();
        collapsedFH.close();

    def getCollapsedOutputFileDir(self):
        return self._collapsedFileName;



