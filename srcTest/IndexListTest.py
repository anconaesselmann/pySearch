import unittest
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.abspath(path.join(__file__, "..", "..")))

from src.IndexList import IndexList

class IndexListTest(unittest.TestCase):
    def test___init__(self):
        print "";
        index = IndexList();
        index.insert('wordA', 'doc1', '12');
        index.insert('wordA', 'doc1', '99');
        index.insert('wordA', 'doc1', '234');

        index.insert('wordA', 'doc5', '19');
        index.insert('wordA', 'doc5', '22');
        index.insert('wordA', 'doc5', '99');

        index.insert('bordA', 'doc9', '1');
        index.insert('wordA', 'doc5', '199');
        index.insert('wordA', 'doc7', '4');
        index.insert('aordA', 'doc7', '88');
        index.insert('wordA', 'doc7', '99');
        index.insert('gordB', 'doc4', '9');
        index.insert('gordD', 'doc7', '23');
        index.insert('gordC', 'doc8', '83');
        index.insert('wordD', 'doc1', '2');
        index.insert('wordD', 'doc7', '11');

        print "";
        index.reset();
        count = 0;
        for term in index:
            # print "Term: " + term.term + " (" + str(term.count) + ")";
            termName      = term.term;
            termFrequency = term.count;
            termString    = termName + ':' + str(termFrequency)
            for doc in term:
                # print "\tDoc: " + doc.doc + " (" + str(doc.count) + ")";
                docId             = doc.doc;
                documentFrequency = doc.count;
                docString         =  '|' + docId + ':' + str(documentFrequency) + ';';
                lineString = '';
                for line in doc:
                    # print "\t\tLine: " + str(line.line);
                    if len(lineString) > 0: lineString += ',';
                    lineString += str(line.line);
                docString  += lineString;
                termString += docString;
            print (termString);

if __name__ == '__main__':
    unittest.main()