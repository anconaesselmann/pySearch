"""
File block allows data to be stored in large chunks with random access pointers
stored in a table.

@author Axel Ancona Esselmann
"""
import io, os, StringIO;
import string, re;


class FileBlock():
    _counter    = 0;
    _extension  = ".txt";

    def __init__(self, blockSize, bufferSize, blocksDir, tableDir):
        self._blockSize            = blockSize;
        self._bufferSize           = bufferSize;
        self._blocksDir            = blocksDir;
        self._tableDir             = tableDir;
        self._recordBuffer         = "";
        self._currentBlockFileName = "";
        self._endOfBlock           = False;
        self._currentBlockFH       = None;
        self._registryAccessMode   = None;
        self._registry             = {};
        self._initTableFileHandler();

    def write(self, id, streamHandler):
        if self._registryAccessMode is not 1:
            self._registryAccessMode = 1;
            self._initTableFileHandler();
        self._updateBlockFileHandler();
        fBegin        = self._counter;
        blockPosBegin = self._currentBlockFH.tell();

        buffer = self._getBuffer(streamHandler);
        while buffer:
            written = self._currentBlockFH.write(buffer);
            self._updateBlockFileHandler();
            buffer = self._getBuffer(streamHandler);

        blockPosEnd        = self._currentBlockFH.tell();
        fEnd               = self._counter;
        record             = FileBlock.FileBlockRecord(id, fBegin, blockPosBegin, fEnd, blockPosEnd);
        self._registry[id] = record;
        self._bufferedRecordWrite(str(record.id) + ";" + str(record.beginFile) + ":" + str(record.beginPos) + "," + str(record.endFile) + ":" + str(record.endPos) + "\n");
        return self._registry;

    def open(self, record):
        if isinstance( record, ( int, long ) ):
            return self.openRecordHandler(record);
        else: return FileBlock.BlockRecordHandle(self._blocksDir, record, self._extension);

    def blockCount(self):
        return self._counter + 1;

    def loadRegistry(self):
        if self._registryAccessMode is not 2:
            self._registryAccessMode = 2;
            self._initTableFileHandler();
        buffer = self._tableFileHandler.readline();
        while buffer:
            idSplit            = string.split(buffer, ';');
            id                 = int(idSplit[0]);
            block1Split        = string.split(idSplit[1], ':');
            block1             = int(block1Split[0]);
            pos1Split          = string.split(block1Split[1], ',');
            pos1               = int(pos1Split[0]);
            block2Split        = string.split(pos1Split[1], ':');
            block2             = int(block2Split[0]);
            pos2               = int(string.strip(block1Split[2]));
            record             = FileBlock.FileBlockRecord(id, block1, pos1, block2, pos2);
            self._registry[id] = record;
            buffer             = self._tableFileHandler.readline();

    def getRecord(self, id):
        return self._registry[id];

    def openRecordHandler(self, id):
        return self.open(self.getRecord(id));

    def _initTableFileHandler(self):
        if self._registryAccessMode == 1:
            self._tableFileHandler = io.open(self._tableDir, 'wb');
        else: self._tableFileHandler = io.open(self._tableDir, 'r');

    def _updateBlockFileHandler(self):
        if self._endOfBlock:
            self._endOfBlock           = False;
            FileBlock._counter        += 1;
            self._currentBlockFileName = self._blocksDir + str(FileBlock._counter) + self._extension;
            self._currentBlockFH       = io.open(self._currentBlockFileName, 'wb');
        elif self._currentBlockFH is None:
            self._currentBlockFileName =  self._blocksDir + str(0) + self._extension;
            self._currentBlockFH       = io.open(self._currentBlockFileName, 'wb');


    def _getBuffer(self, currentFH):
        emptySpace = self._blockSize - self._currentBlockFH.tell();
        if emptySpace <= self._bufferSize:
            bufferSize       = emptySpace;
            self._endOfBlock = True;
        else: bufferSize = self._bufferSize;
        buffer = currentFH.read(bufferSize);
        return buffer;

    def _bufferedRecordWrite(self, recordString):
        spaceInBuffer = self._bufferSize - len(self._recordBuffer);
        recStringLen  = len(recordString);
        if recStringLen == 0: return;
        elif recordString < spaceInBuffer:
            self._recordBuffer += recordString;
        else:
            self._recordBuffer += recordString[0:spaceInBuffer];
            self._tableFileHandler.write(self._recordBuffer);
            self._recordBuffer = "";
            newRecordString    = recordString[spaceInBuffer:];
            self._bufferedRecordWrite(newRecordString);


    class FileBlockRecord():
        def __init__(self, id = None, beginFile = None, beginPos = None, endFile = None, endPos = None):
            self.beginFile = beginFile;
            self.beginPos  = beginPos;
            self.endFile   = endFile;
            self.endPos    = endPos;
            self.id        = id;

    class BlockRecordHandle():
        s_openFileId     = None;
        s_openFileHandle = None;
        def __init__(self, blocksDir, record, extension, bufferSize=100000):
            self._record     = record;
            self._openFileId = None;
            self._readHead   = None;
            self._blocksDir  = blocksDir;
            self._extension  = extension;
            self._eof        = False;
            self._readHead   = record.beginPos;
            self.setBufferSize(bufferSize);
            if FileBlock.BlockRecordHandle.s_openFileId == None or record.beginFile != FileBlock.BlockRecordHandle.s_openFileId:
                self._updateBlockFileHandle();
            else:
                self._currentBlockFH = FileBlock.BlockRecordHandle.s_openFileHandle;

        def read(self, bufferSize):
            if self._eof: return '';
            if self._openFileId == self._record.endFile:
                if self._readHead + bufferSize > self._record.endPos:
                    bufferSize = self._record.endPos - self._readHead;
            self._currentBlockFH.seek(self._readHead);
            buffer    = self._currentBlockFH.read(bufferSize);
            bytesRead = len(buffer);
            self._readHead += bytesRead;
            if bytesRead < bufferSize:
                self._updateBlockFileHandle();
                buffer += self.read(bufferSize - bytesRead);
            return buffer;

        def setBufferSize(self, bufferSize):
            self._bufferSize = bufferSize;

        # Currently does not read lines longer than buffer size.
        def readline(self):
            buffer = self.read(self._bufferSize);
            try:
                lbPos = buffer.index('\n');
            except ValueError, e:
                lbPos = self._bufferSize;

            return buffer[0:lbPos];


        def _updateBlockFileHandle(self):
            if self._openFileId is None:
                self._openFileId = self._record.beginFile;
                self._readHead   = self._record.beginPos;
            elif self._openFileId < self._record.endFile:
                self._openFileId += 1;
                self._readHead = 0;
            else: self._eof = True;
            self._currentBlockFH = io.open(self._blocksDir + str(self._openFileId) + self._extension, 'rb');
            FileBlock.BlockRecordHandle.s_openFileId     = self._openFileId;
            FileBlock.BlockRecordHandle.s_openFileHandle = self._currentBlockFH;

