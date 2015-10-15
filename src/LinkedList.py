"""
@author Axel Ancona Esselmann
"""
class LinkedList():
    def __init__(self):
        self.next         = None;
        self._currentNode = None;
        self._temp        = None;

    def __str__(self):
        return self.toString(',');

    def _insert(self,old, new):
        temp     = old.next;
        old.next = new;
        new.next = temp;

    def insert(self, value):
        newNode = LinkedList.Node(value);
        if not self.next or value < self.next.value:
            self._insert(self, newNode);
        else:
            currentNode = self.next;
            while currentNode.next is not None and value > currentNode.next.value:
                currentNode = currentNode.next;
            self._insert(currentNode, newNode);

    def insertAtHead(self, value):
        newNode = LinkedList.Node(value);
        if self._currentNode is None:
            newNode.next = self.next;
            self.next    = newNode;
        else: self._insert(self._currentNode, newNode);

    def getItem(self, value):
        if self.next == None:
            self._currentNode = None;
            return None;
        currentNode = prevNode = self.next
        if currentNode.value > value:
            self._currentNode = None;
        elif currentNode.next is None:
            self._currentNode = self.next;
        else:
            while currentNode is not None and value >= currentNode.value:
                prevNode    = currentNode;
                currentNode = currentNode.next;
            if value == prevNode.value:
                self._currentNode = prevNode;
                return self._currentNode.value;
            else:
                self._currentNode = prevNode;
        return None;

    def toString(self, seperator):
        out = '';
        currentNode = self.next;
        hasOutput = False;
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

