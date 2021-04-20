"""
LeetCode :: 707 :: Design Linked List
"""
from collections import namedtuple
Node = namedtuple('Node', ['val', 'next'])

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index):
        return self._get(self.head, index)

    def _get(self, node, index):
        if node is None:
            return -1
        elif index < 0:
            return -1
        elif index == 0:
            return node.val
        else:
            return self._get(node.next, index - 1)
    
    def addAtHead(self, val):
        self.head = Node(val, self.head)

    def addAtTail(self, val):
        self.head = self._addAtTail(self.head, val)

    def _addAtTail(self, node, val):
        if node is None:
            return Node(val, None)
        else:
            return Node(node.val, self._addAtTail(node.next, val))

    def deleteAtIndex(self, index):
        if index < 0:
            return
        self.head = self._deleteAtIndex(self.head, index)

    def _deleteAtIndex(self, node, index):
        if node is None:
            return None
        elif index == 0:
            return node.next
        else:
            return Node(node.val, self._deleteAtIndex(node.next, index - 1))

    def addAtIndex(self, index, val):
        if index < 0:
            index = 0
        self.head = self._addAtIndex(self.head, index, val)

    def _addAtIndex(self, node, index, val):
        if index == 0:
            return Node(val, node)
        elif node is None:
            return None
        else:
            return Node(node.val, self._addAtIndex(node.next, index - 1, val))
