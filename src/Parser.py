"""
Parser can parse sections of a document collection into partitions that can then be inverted by Inverters.

@author Axel Ancona Esselmann
"""
import PartitionTable;
import io

class Parser():
    def __init__(self, tokenizer, outputDir, stopWords = None, stemmer = None, partitionTable = None):
        self._tokenizer      = tokenizer;
        self._stemmer        = stemmer;
        self._outputDir      = outputDir;
        self._partitionTable = partitionTable;
        self._stopWordsList  = stopWords;
        self._separationChar = ',';
        self._partitionFileHandlers = {};
        self._nbrDocumentsParsed = 0;
        self._outputFileNames = [];

        for i in xrange(0,self._partitionTable.getNbrPartitions()):
            fileName = self._outputDir + str(i) + self._partitionTable.getPartitionExtension();
            self._outputFileNames.append(fileName);
            self._partitionFileHandlers[i] = io.open(fileName, 'wb');

    def parse(self, documentCollection):
        docTokenCountFH = io.open(self._outputDir + "inverter_1_docTokenCount_temp.txt", 'wb');
        document = documentCollection.nextDocument();
        while document is not None:
            documentName = document.getName();
            self._tokenizer.loadDocument(document);
            token, tokenPosition = self._tokenizer.nextToken();
            while token is not None:
                if self._stopWordsList is not None:
                    if self._stopWordsList.isStopWord(token):
                        token, tokenPosition = self._tokenizer.nextToken();
                        continue;
                partitionId = self._partitionTable.getPartitionId(token);
                if self._stemmer is not None: token = self._stemmer.stem(token);
                termDocPositionString = token + self._separationChar + documentName + self._separationChar +  str(self._tokenizer._tokenPosition) + '\n';
                self._partitionFileHandlers[partitionId].write(termDocPositionString);
                token, tokenPosition = self._tokenizer.nextToken();
            document = documentCollection.nextDocument();
            self._nbrDocumentsParsed += 1;
            docTokenCountLine = documentName + "," + str(self._tokenizer._tokenPosition) + "\n";
            docTokenCountFH.write(docTokenCountLine);
        self._partitionFileHandlers[partitionId].close();

    def getOutputFileNames(self):
        return self._outputFileNames;

    def getNbrDocumentsParsed(self):
        return self._nbrDocumentsParsed;