"""
SearchEngine works with an inverted index produced by Indexer.

Two word and queries can be searched for.

@author Axel Ancona Esselmann
"""
import io, math;
from LinkedList import LinkedList;
from QueryTokenizer import QueryTokenizer;
from QueryTerm import QueryTerm;
from ProximityQueryTerm import ProximityQueryTerm;
from IndexList import IndexList;
import os.path;

class QueryResultItem():
    def __init__(self,docId,tfidf):
        self.docId = docId;
        self.tfidf = tfidf;
    def __lt__(self, other):
        return self.tfidf <  other.tfidf;
    def __eq__(self, other):
        return self.tfidf  == other.tfidf;
    def __str__(self):
        return "Document id: " + str(self.docId) + ", tf.idf: " + str(self.tfidf);

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
        self._tempDir = os.path.dirname(os.path.dirname(dictionaryDir)) + "/invTemp/";
        self._queryTokenizer = queryTokenizer;
        self.termFrequencies = None;
        self._documentCount = 0;
        self._loadDocumentTermFrequencies();
        self._docCollect   = None;
        self._tokenizer    = None;
        self._currentQueryId = 0;

    """
    returns an array of documents that the two query terms are both in
    """
    def search(self, query, queryExpansionParameter):
        orderedQueryResults                      = self.tfidf(query);
        mostRelevantDocumentId                   = orderedQueryResults.getHead().docId;
        mostRelevantDocumentIdDocumentCollection = int(self._documentIds[mostRelevantDocumentId]);
        orderedExpansionTerms                    = LinkedList();
        orderedExpansionTerms.printSep           = "\n";

        uniqueTerms  = {};
        currentDoc   = self._docCollect.nextDocument();
        currentDocId = int(currentDoc.getName());
        while currentDocId != mostRelevantDocumentIdDocumentCollection:
            currentDoc   = self._docCollect.nextDocument();
            currentDocId = int(currentDoc.getName());

        # current doc now has the document that is the highest ranked tfid result
        self._tokenizer.loadDocument(currentDoc);

        # generate unique query term set
        token, position = self._tokenizer.nextToken()
        while token is not None:
            uniqueTerms[token] = position;
            token, position = self._tokenizer.nextToken();

        # calculate tfidf scores for each token and insert into ordered linked list
        for token, pos in uniqueTerms.iteritems():
            tfidf = self.tfidf_term(token, mostRelevantDocumentIdDocumentCollection);
            orderedExpansionTerms.insertSorted(QueryResultItem(token, tfidf));

        # expand query with most relevant query terms:
        currentNode = orderedExpansionTerms._head;
        for i in xrange(0,queryExpansionParameter):
            currentData = currentNode.value.docId;
            query += " " + currentData;
            currentNode = currentNode.next;

        # perform search with appended query
        self._currentQueryId += 1;

        results = self.tfidf(query);



    def tfidf_term(self, query, docId):
        queryTokens  = self._queryTokenizer.tokenize(query);
        postingLists = self._getPostingLists(queryTokens);
        documentScores = {};
        for term in postingLists:
            if term is None: continue
            for doc in term:
                if str(doc.doc) != str(docId): continue;
                termFrequency = 1 + math.log10(float(doc.count) / float(self.termFrequencies[int(doc.doc) - 1]))
                docSocre = termFrequency * self._getIDF(term);
                return docSocre;
        return 0;

    def setDocCollect(self, docCollect):
        docCollect.reset();
        self._docCollect = docCollect;

    def setTokenizer(self, tokenizer):
        self._tokenizer = tokenizer;

    def tfidf(self, query):
        queryTokens  = self._queryTokenizer.tokenize(query);
        postingLists = self._getPostingLists(queryTokens);
        documentScores = {};
        # create document scores
        for term in postingLists:
            for doc in term:
                termFrequency = 1 + math.log10(float(doc.count) / float(self.termFrequencies[int(doc.doc) - 1]))
                docSocre = termFrequency * self._getIDF(term);
                if str(doc.doc) in documentScores.keys(): documentScores[str(doc.doc)] += docSocre;
                else: documentScores[str(doc.doc)] = docSocre;
        # create an ordered list of documents, ordered by document score
        orderedQueryResults = LinkedList();
        orderedQueryResults.printSep = "\n";
        for docId, ds in documentScores.iteritems():
            orderedQueryResults.insertSorted(QueryResultItem(docId, ds));
        return orderedQueryResults


    def _getIDF(self, term):
        if float(term.count) == 0: return 0;
        return math.log10(float(self._documentCount) / float(term.count));

    def _reloadDictionary(self, dictionaryDir):
        self._dictionary      = {};
        self._documentIds     = {};
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


    def _loadDocumentTermFrequencies(self):
        self.termFrequencies = {};
        docTermCountFH = io.open(os.path.join(os.path.dirname(self._tempDir), "inverter_1_docTokenCount.txt"), "rb");
        docCountFH = io.open(os.path.join(os.path.dirname(self._tempDir), "inverter_1_docTotalDocCount.txt"), "rb");
        while True:
            line = docTermCountFH.readline()
            lineParts = line.rstrip().split(",")
            if not line: break
            self.termFrequencies[int(lineParts[0])] = int(lineParts[1]);
        line = docCountFH.readline();
        self._documentCount = int(line);
        docTermCountFH.close();
        docCountFH.close();
