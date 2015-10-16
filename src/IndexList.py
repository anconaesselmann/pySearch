"""
Provides functionality to deal with Term Document and Line

@author Axel Ancona Esselmann
"""
from LinkedList import LinkedList;
class IndexList():
    def __init__(self):
        self.objs      = LinkedList();
        self._iterator = None;
    def __str__(self):
        return self.objs.toString('\n');
    def reset(self):
        self.objs.reset();
    def insert(self, string1, string2, string3):
        obj = IndexList.Term(string1);
        current = self.objs.getLastItemOf(obj);
        if current:
            current.count += 1;
        else:
            self.objs.insertSorted(obj);
            current = obj;
        current.insertDoc(string2, string3);

    def __iter__(self):
        return self;
    def next(self):
        if self._iterator is None:
            if self.objs._head is None: raise StopIteration
            self._iterator = self.objs._head;
            return self._iterator.value;
        self._iterator = self._iterator.next;
        if self._iterator is None: raise StopIteration
        return self._iterator.value;

    class Term():
        def __init__(self, term):
            self.term  = term;
            self.docs  = LinkedList();
            self.count = 1;
            self._iterator = None;
            self._temp = None;
        def __str__(self):
            return "Term: " + self.term + ', count:' + str(self.count) + self.docs.toString(',');
        def __lt__(self, other):
            return self.term <  other.term;
        def __eq__(self, other):
            return self.term  == other.term;

        def insertDoc(self, doc, line):
            obj = IndexList.Doc(doc);
            current = self.docs.getLastItemOf(obj);
            if current:
                current.count += 1;
            else:
                self.docs.insertSorted(obj);
                current = obj;
            current.insertLine(line);

        def __iter__(self):
            return self;
        def next(self):
            if self._temp is None:
                if self.terms is None: raise StopIteration
                self._temp = self.terms;
            if self._temp._currentNode is None: raise StopIteration
            value = self._temp._currentNode.value;
            self._temp._currentNode = self._temp._currentNode.next;
            return value;

        def __iter__(self):
            return self;
        def next(self):
            if self._iterator is None:
                if self.docs._head is None: raise StopIteration
                self._iterator = self.docs._head;
                return self._iterator.value;
            self._iterator = self._iterator.next;
            if self._iterator is None: raise StopIteration
            return self._iterator.value;

    class Doc():
        def __init__(self, doc):
            self.doc   = doc;
            self.lines = LinkedList();
            self.count = 1;
            self._iterator = None;
        def __str__(self):
            return '\n\t' + self.doc + ', count:' + str(self.count) + self.lines.toString(',');
        def __lt__(self, other):
            return self.doc < other.doc;
        def __eq__(self, other):
            return self.doc  == other.doc;

        def insertLine(self, line):
            line = IndexList.Line(int(line));
            self.lines.insertSorted(line);

        def __iter__(self):
            return self;
        def next(self):
            if self._iterator is None:
                if self.lines._head is None: raise StopIteration
                self._iterator = self.lines._head;
                return self._iterator.value;
            self._iterator = self._iterator.next;
            if self._iterator is None: raise StopIteration
            return self._iterator.value;

    class Line():
        def __init__(self, line):
            self.line  = line;
        def __str__(self):
            return '\n\t\t' + str(self.line);
        def __lt__(self, other):
            return self.line < other.line;
        def __eq__(self, other):
            return self.line == other.line;