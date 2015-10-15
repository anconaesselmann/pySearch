"""
A partition Table used to split up work for Parsers and Inverters

@author Axel Ancona Esselmann
"""
class PartitionTable():
    def __init__(self, partitions):
        self._partitions = partitions;
        self._nbrPartitions = len(partitions);
        self._partitonExtension = '.txt';

    def getPartitionId(self, token):
        for i in xrange(0,self._nbrPartitions):
            if token < self._partitions[i]: return i;
        return self._nbrPartitions;

    def getNbrPartitions(self):
        return self._nbrPartitions + 1;

    def setPartitionExtension(self, extension):
        self._partitonExtension = extension;

    def getPartitionExtension(self):
        return self._partitonExtension;