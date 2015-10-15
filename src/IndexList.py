"""
Provides functionality to deal with Term Document and Line

@author Axel Ancona Esselmann
"""
from LinkedList import LinkedList;
class IndexList():
    def __init__(self):
        self.terms = LinkedList();
        self._temp = None;
    def __str__(self):
        return self.terms.toString('\n');
    def insert(self, string1, string2, string3):
        term = IndexList.Term(string1);
        existingTerm = self.terms.getItem(term);
        if existingTerm is None:
            term.insertDoc(string2, string3);
            self.terms.insertAtHead(term);
        else:
            existingTerm.count += 1;
            existingTerm.insertDoc(string2, string3);

    def __iter__(self):
        return self;

    def next(self):
        if self._temp is None:
            if self.terms is None: raise StopIteration
            self._temp = self.terms;
        self._temp = self._temp.next;
        if self._temp is None: raise StopIteration
        return self._temp.value;

    class Term():
        def __init__(self, term):
            self.term  = term;
            self.docs  = LinkedList();
            self.count = 1;
        def __str__(self):
            return "Term: " + self.term + ' ' + str(self.count) + self.docs.toString(',');
        def __lt__(self, other):
            return self.term <  other.term;
        def __eq__(self, other):
            return self.term  == other.term;
        def insertDoc(self, doc, line):
            doc         = IndexList.Doc(doc);
            existingDoc = self.docs.getItem(doc);
            if existingDoc is None:
                doc.insertLine(line);
                self.docs.insertAtHead(doc);
            else:
                existingDoc.count += 1;
                existingDoc.insertLine(line);

    class Doc():
        def __init__(self, doc):
            self.doc   = doc;
            self.lines = LinkedList();
            self.count = 1;
        def __str__(self):
            return '\n\t' + self.doc + ',' + str(self.count) + self.lines.toString(',');
        def __lt__(self, other):
            return self.doc < other.doc;
        def __eq__(self, other):
            return self.doc  == other.doc;
        def insertLine(self, line):
            line = IndexList.Line(line);
            self.lines.insert(line);

    class Line():
        def __init__(self, line):
            self.line  = line;
        def __str__(self):
            return '\n\t\t' + str(self.line);
        def __lt__(self, other):
            return self.line < other.line;
        def __eq__(self, other):
            return self.line == other.line;