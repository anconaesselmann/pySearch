"""
@author Axel Ancona Esselmann
"""
class LinkedList():
    def __init__(self):
        self._currentNode = None;
        self._head        = None;

    def __str__(self):
        return self.toString(',');

    def reset(self):
        self._currentNode = self._head;

    def insertAfter(self, value):
        newNode = LinkedList.Node(value);
        if self._head is None:
            self._head = newNode;
            self._currentNode = self._head;
            return;
        else:
            newNode.next = self._currentNode.next
            self._currentNode.next = newNode;
            self._currentNode = newNode;
            return;

    def insertSorted(self, value):
        if self._head is None: self.insertAfter(value);
        else:
            newNode = LinkedList.Node(value);
            if self._head.value > value:
                newNode.next = self._head;
                self._head = newNode;
            else:
                current = self._head;
                while current is not None:
                    next = current.next;
                    if next is None: break;
                    if value < next.value: break
                    current = current.next;
                newNode.next = current.next
                current.next = newNode;
                current = newNode;

    def hasItem(self, value):
        current = self._head;
        while current is not None:
            if current.value == value: return True;
            current = current.next;
        return False;

    def getLastItemOf(self, value):
        current = self._head;
        while current is not None:
            if current.value == value:
                if current.next is not None:
                    next = current.next.value;
                    while next is not None and next == value:
                        current = next;
                        next = current.next;
                return current.value;
            current = current.next;
        return None

    def toString(self, seperator):
        out = '';
        hasOutput = False;
        currentNode = self._head;
        while currentNode is not None:
            if not hasOutput:
                out += str(currentNode.value);
                hasOutput = True;
            else: out += seperator + str(currentNode.value);
            currentNode = currentNode.next;
        return out;

    class Node():
        def __init__(self, value):
            self.next  = None;
            self.value = value;
        def __str__(self):
            return str(self.value);

