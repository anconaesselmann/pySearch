"""
SearchEngine works with an inverted index produced by Indexer.

Two word and queries can be searched for.

@author Axel Ancona Esselmann
"""
import io;
from LinkedList import LinkedList;
from QueryTokenizer import QueryTokenizer;
from QueryTerm import QueryTerm;
from ProximityQueryTerm import ProximityQueryTerm;

class SearchEngine():
    def __init__(self, dictionaryDir, postingList, stemmer, stopWordsList, docIdFileName, queryTokenizer):
        self._postingList     = postingList;
        self._stemmer         = stemmer;
        self._stopWordsList   = stopWordsList;
        self._dictionary      = None;
        self._documentIds     = None;
        self._docIdFileName   = docIdFileName;
        self._reloadDictionary(dictionaryDir);
        self._queryTokenizer = queryTokenizer;

    """
    returns an array of documents that the two query terms are both in
    """
    def search(self, query):
        queryTokens = self._queryTokenizer.tokenize(query);
        print("tokens:")
        # print(queryTokens);
        for qt in queryTokens:
            print(str(qt));
        postingLists = self._getPostingLists(queryTokens);

        # terms   = query.split(' ');
        # l1      = self._getPostingList(terms[0]);
        # l2      = self._getPostingList(terms[1]);
        # p1      = l1._head;
        # p2      = l2._head;
        # results = [];
        # while (p1 is not None) and (p2 is not None):
        #     if p1.value == p2.value:
        #         results.append(p1.value);
        #         p1 = p1.next;
        #         p2 = p2.next;
        #     else:
        #         if p1.value < p2.value: p1 = p1.next;
        #         else: p2 = p2.next;
        # return results;

    def _reloadDictionary(self, dictionaryDir):
        self._dictionary      = {};
        self._documentIds      = {};
        fh = io.open(dictionaryDir, 'r');
        line = fh.readline();
        while line:
            parts = line.split(',');
            self._dictionary[parts[0]] = int(parts[1]);
            line = fh.readline();

        fh = io.open(self._docIdFileName, 'r');
        line = fh.readline();
        while line:
            parts = line.split(',');
            self._documentIds[parts[0]] = int(parts[1]);
            line = fh.readline();

    def _getPostingLists(self, queryTokens):
        pLists = [];
        return pLists;

    """
    Returns a linked list of documents that have token in it
    """
    def _getPostingList(self, token):
        stemmedToken = self._stemmer.stem(token);
        if self._stopWordsList.isStopWord(stemmedToken): return None;
        fileHandler = self._postingList.openRecordHandler(self._dictionary[stemmedToken]);
        line        = fileHandler.readline();
        parts       = line.split('|');
        list        = LinkedList();
        for i in xrange(1, len(parts)):
            docParts = parts[i].split(':');
            list.insertAfter(self._documentIds[docParts[0]]);
        return list;

