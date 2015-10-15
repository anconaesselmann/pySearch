"""
@author Axel Ancona Esselmann

requires:
    https://pypi.python.org/pypi/loremipsum/#downloads

    or: $sudo python /Dropbox/reinstall/lorem/setup.py install
"""
class RandomParagraph():
    def get(self, min, max):
        import loremipsum
        sentences_count, words_count, paragraph = loremipsum.generate_paragraph();
        print sentences_count;
        print words_count;
        return paragraph;

class RandomText():
    paragraphCount = 5;
    def get(self):
        import loremipsum
        text = loremipsum.get_paragraphs(self.paragraphCount);

        return '\n'.join(text);


import io, os, StringIO;
class RandomFile():
    _counter = 0;
    _ending = "";
    _contentGenerator = None;
    _fileHandler = None;
    _baseDir = "";
    _bufferSize = 2;
    def __init__(self, baseDir, contentGenerator):
        self._contentGenerator = contentGenerator;
        self._baseDir = baseDir;
        self._fileName = "";

    def setExtension(self, ending):
        self._ending = ending;

    def setBufferSize(self, testSuite):
        self._bufferSize = testSuite["bufferSize"];

    def create(self):
        self._fileName    = self._baseDir + str(RandomFile._counter) + self._ending;
        self._fileHandler = io.open(self._fileName, 'wb');
        text              = self._contentGenerator.get();
        stringHandler     = StringIO.StringIO();

        stringHandler.write(text);
        stringHandler.seek(0);
        buffer = stringHandler.read(self._bufferSize);
        while buffer:
            self._fileHandler.write(buffer);
            buffer = stringHandler.read(self._bufferSize);
        RandomFile._counter += 1;
        self._fileHandler.close();

    def delete(self):
        self._fileHandler.close();
        os.remove(self._fileName);