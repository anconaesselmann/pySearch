"""
@author Axel Ancona Esselmann
"""

from Timing import Timing;
from src.Random import RandomText, RandomFile;
import timeit
from os import sys, path
import io;
from src.FileBlock import FileBlock;
from random import shuffle, expovariate;

class FileAccess():
    def description(self, output):
        t = Timing(False);


        t.out("""
Testing individual file access or block access with random access:

Testing scenarios:

- A high probability that the data is in a few of many block files
- A the probability for all blocks is the same
- Each datum is in it's own file (test small, large and varying data size)

- test all scenarios with a variety of buffer sizes, block file sizes and data length.""");

    def individualFiles(self, testSuite):
        t = Timing(testSuite['output']);

        individualDir = testSuite['dir'] + ".individualFilesDynamic" + path.sep;

        t.out("\n\nScenario: Each datum is in it's own file which is accessed sequentially.");
        t.start();
        for n in xrange(0,testSuite['nbrFiles']):
            fh = io.open(individualDir + str(testSuite['shuffledIdArray'][n]) + testSuite['extension'], 'r');
            buffer = fh.read(testSuite['bufferSize']);
            fh.close();
        print "\tresult for sequential indiv. file access: " + str(t.stop());

        t.out("Scenario: Each datum is in it's own file which is accessed randomly.");
        t.start();
        for n in xrange(0,testSuite['nbrFiles']):
            fh = io.open(individualDir + str(n) + testSuite['extension'], 'r');
            buffer = fh.read(testSuite['bufferSize']);
            fh.close();
        print "\tresult for sequential indiv. file access: " + str(t.stop());

    def blockFiles(self, testSuite):
        t = Timing(testSuite['output']);

        fb = FileBlock(
            testSuite['blockSize'],
            testSuite['bufferSize'],
            testSuite['blockFilesDir'],
            testSuite['tableFileName'],
        );
        fb.loadRegistry();

        t.out("\n\nScenario: Large block files, files are accessed sequentially.");
        t.start();
        for n in xrange(0,testSuite['nbrFiles']):
            fh = fb.open(n);
            buffer = fh.read(testSuite['bufferSize']);
        print "\tresult for sequential block file access:  " + str(t.stop());

        t.out("Scenario: Large block files, files are accessed sequentially in reverse order.");
        t.start();
        for n in xrange(testSuite['nbrFiles']-1,-1,-1):
            fh = fb.open(n);
            buffer = fh.read(testSuite['bufferSize']);
        print "\tresult for reverse sequential block file access:  " + str(t.stop());

        t.out("Scenario: Large block files, files are accessed randomly.");
        t.start();
        for n in xrange(0,testSuite['nbrFiles']):
            fh = fb.open(testSuite['shuffledIdArray'][n]);
            buffer = fh.read(testSuite['bufferSize']);
        print "\tresult for random block file access:  " + str(t.stop());



