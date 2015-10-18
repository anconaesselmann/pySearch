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
from IndexList import IndexList;

class PostingListEntry():
    def __init__(self, documentId, termPosition):
        self.documentId   = documentId;
        self.termPosition = termPosition;

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
        postingLists = self._getPostingLists(queryTokens);
        for term in postingLists:
            tf = self._getTF(term);
            # idf = self._getIDF()
            print term;

    def _getTF(self, term):
        termFrequencies = {};
        for doc in term:
            print "occurances in document: " + str(doc.doc) + " " + str(doc.count)

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
        for qToken in queryTokens:
            if isinstance(qToken, QueryTerm):
                pLists.append(self._getQueryTermPostingList(qToken.term));
            elif isinstance(qToken, ProximityQueryTerm):
                list1, list2 = self._getProximityQueryTermPostingList(qToken.term1, qToken.term2, qToken.distance)
                if list1 is not None:
                    pLists.append(list1);
                    pLists.append(list2);
                    pass
        return pLists;

    """
    Returns a linked list of documents that have token in it
    """
    def _getQueryTermPostingList(self, token):
        stemmedToken = self._stemmer.stem(token);
        if self._stopWordsList.isStopWord(stemmedToken): return None;
        fileHandler = self._postingList.openRecordHandler(self._dictionary[stemmedToken]);
        line        = fileHandler.readline();
        parts       = line.split('|');
        documentFrequency = parts[0].split(':')[1];
        term = IndexList.Term(token)
        term.count = documentFrequency
        for i in xrange(1, len(parts)):
            docParts   = parts[i].split(':');
            docDetails = (docParts[1]).split(';');
            lines = docDetails[1].split(',');
            for i in xrange(0, len(lines)):
                term.insertDoc(self._documentIds[docParts[0]], lines[i]);
        return term;

    def _getProximityQueryTermPostingList(self, term1String, term2String, distance):
        term1   = self._getQueryTermPostingList(term1String);
        term2   = self._getQueryTermPostingList(term2String);
        docs1    = term1.docs._head;
        docs2    = term2.docs._head;
        newDocs1 = LinkedList();
        newDocs2 = LinkedList();
        termHasDocs = False
        while (docs1 is not None) and (docs2 is not None):
            if docs1.value == docs2.value:
                if self._docHasTokensWithinDistance(docs1.value, docs2.value, distance):
                    newDocs1.insertAfter(docs1.value);
                    newDocs2.insertAfter(docs2.value);
                    termHasDocs = True;
                docs1 = docs1.next;
                docs2 = docs2.next;
            else:
                if docs1.value < docs2.value: docs1 = docs1.next;
                else: docs2 = docs2.next;
        # transfer term count per document to truncated list
        newDocs1.count = term1.count
        newDocs2.count = term2.count
        # exchange full document term count with truncated list
        term1.docs = newDocs1;
        term2.docs = newDocs2;
        if termHasDocs: return term1, term2;
        else: return None, None


    def _docHasTokensWithinDistance(self, doc1, doc2, distance):
        lines1 = doc1.lines._head;
        lines2 = doc2.lines._head;
        while (lines1 is not None) and (lines2 is not None):
            if lines2.value.line <= lines1.value.line: lines2 = lines2.next; # pos of token 2 is before pos of token 1
            else:
                if lines2.value.line <= lines1.value.line + distance + 1: return True;
                else: lines1 = lines1.next; # pos of token 2 is too far away
        return False;
