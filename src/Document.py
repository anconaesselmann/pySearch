"""
@author Axel Ancona Esselmann
"""
import abc;

class Document(object):
    __metaclass__ = abc.ABCMeta;
    @abc.abstractmethod
    def getName(self):
        raise NotImplementedError('getName has to be defined');

    @abc.abstractmethod
    def getChar(self):
        raise NotImplementedError('getChar has to be defined');

    @abc.abstractmethod
    def ungetChar(self):
        raise NotImplementedError('ungetChar has to be defined');

    @abc.abstractmethod
    def isEOF(self):
        raise NotImplementedError('ungetChar has to be defined');
