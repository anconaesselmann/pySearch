"""
Comparing the runtime of different methodologies for reading terId, docId and position from a stream.

@author Axel Ancona Esselmann
"""
from Timing import Timing;
import StringIO, re;
class regex():
    def __init__(self):
        print

    def regexLineSplit(self, testSuite):
        t = Timing(testSuite['output']);

        t.out('\nRegex timing:');
        compiledExpression = re.compile(r"""
            (?P<termId>\d*),
            (?P<docId>\d*),
            (?P<position>\d*)
        """, re.S|re.X)
        stringHandler = StringIO.StringIO(testSuite['lines']);

        t.start();
        line = stringHandler.readline();
        while line:
            match  = re.match(compiledExpression, line)
            termId = int(match.group('termId'));
            docId  = int(match.group('docId'));
            posit  = int(match.group('position'));
            # print str(termId) + "," + str(docId) + "," + str(posit);
            line = stringHandler.readline();
        print "Result: " + str(t.stop()) + '\n';

    def stringIOLineSplit(self, testSuite):
        t = Timing(testSuite['output']);
        t.out('\nStringIO timing:');

        t.start();
        stringHandler = StringIO.StringIO(testSuite['lines']);

        t.start();
        line = stringHandler.readline();
        while line:
            lineHandler = StringIO.StringIO(line);
            char = lineHandler.read(1);
            while char:
                char = lineHandler.read(1);
            line = stringHandler.readline();

        print "Result: " + str(t.stop()) + '\n';

    def split(self, testSuite):
        t = Timing(testSuite['output']);
        t.out('\nSplit timing:');

        t.start();
        stringHandler = StringIO.StringIO(testSuite['lines']);

        t.start();
        line = stringHandler.readline();
        while line:
            s = line.split(',');
            termId = int(s[0]);
            docId  = int(s[1]);
            posit  = int(s[2]);
            # print str(termId) + "," + str(docId) + "," + str(posit);
            line = stringHandler.readline();

        print "Result: " + str(t.stop()) + '\n';

    def arrayRead(self, testSuite):
        t = Timing(testSuite['output']);
        t.out('\nSplit timing:');

        array = range(0,testSuite['nbrLines']);
        t.start();
        for x in xrange(0,testSuite['nbrLines']):
            a = array[x];
        time1 = t.stop();
        t.start();
        for x in xrange(0,testSuite['nbrLines']):
            a = array[x];
        time2 = t.stop();
        t.start();
        for x in xrange(0,testSuite['nbrLines']):
            a = array[x];
        time3 = t.stop();
        t.start();
        for x in xrange(0,testSuite['nbrLines']):
            a = array[x];
        time4 = t.stop();
        t.start();
        for x in xrange(0,testSuite['nbrLines']):
            a = array[x];
        time5 = t.stop();
        t.start();
        for x in xrange(0,testSuite['nbrLines']):
            a = array[x];
        time6 = t.stop();

        r1 = time1 - time1;
        r2 = time2 - time1;
        r3 = time3 - time1;
        r4 = time4 - time1;
        r5 = time5 - time1;
        r6 = time6 - time1;
        print (r2 + r3 + r4 + r5 + r6) / 5;
        # print r1;
        # print r2;
        # print r3;
        # print r4;
        # print r5;
        # print r6;

