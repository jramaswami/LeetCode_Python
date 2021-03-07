"""
LeetCode :: March 2021 Challenge :: Design Hashmap
jramaswami
"""
from typing import *
from collections import namedtuple


Node = namedtuple('Node', ['key', 'val', 'left', 'right'])


def put0(node, key, val):
    """Recursive function to place node in tree."""
    if node is None:
        return Node(key, val, None, None)
    elif node.key == key:
        return Node(node.key, val, node.left, node.right)
    elif key < node.key:
        return Node(node.key, node.val, put0(node.left, key, val), node.right)
    elif key > node.key:
        return Node(node.key, node.val, node.left, put0(node.right, key, val))


def get0(node, key):
    """Recursive function to search for key in tree."""
    if node is None:
        return -1
    elif node.key == key:
        return node.val
    elif key < node.key:
        return get0(node.left, key)
    elif key > node.key:
        return get0(node.right, key)


def del0(node, key):
    """
    Recursive function to delete node.  For convenience, just put a tombstone
    in the value.
    """
    if node is None:
        return None
    elif node.key == key:
        return Node(node.key, -1, node.left, node.right)
    elif key < node.key:
        return Node(node.key, node.val, del0(node.left, key), node.right)
    elif key > node.key:
        return Node(node.key, node.val, node.left, del0(node.right, key))


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = None

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.root = put0(self.root, key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return get0(self.root, key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.root = del0(self.root, key)
        
#
# Testing
#
null = None


def test_1():
    hashMap = MyHashMap()
    hashMap.put(1, 1)
    hashMap.put(2, 2)         
    assert hashMap.get(1) == 1
    hashMap.get(3) == -1
    hashMap.put(2, 1)
    assert hashMap.get(2) == 1 
    hashMap.remove(2)
    assert hashMap.get(2) == -1


def test_2():
    methods = ["MyHashMap","remove","put","remove","remove","get","remove","put","get","remove","put","put","put","put","put","put","put","put","put","put","put","remove","put","put","get","put","get","put","put","get","put","remove","remove","put","put","get","remove","put","put","put","get","put","put","remove","put","remove","remove","remove","put","remove","get","put","put","put","put","remove","put","get","put","put","get","put","remove","get","get","remove","put","put","put","put","put","put","get","get","remove","put","put","put","put","get","remove","put","put","put","put","put","put","put","put","put","put","remove","remove","get","remove","put","put","remove","get","put","put"]
    arguments = [[],[27],[65,65],[19],[0],[18],[3],[42,0],[19],[42],[17,90],[31,76],[48,71],[5,50],[7,68],[73,74],[85,18],[74,95],[84,82],[59,29],[71,71],[42],[51,40],[33,76],[17],[89,95],[95],[30,31],[37,99],[51],[95,35],[65],[81],[61,46],[50,33],[59],[5],[75,89],[80,17],[35,94],[80],[19,68],[13,17],[70],[28,35],[99],[37],[13],[90,83],[41],[50],[29,98],[54,72],[6,8],[51,88],[13],[8,22],[85],[31,22],[60,9],[96],[6,35],[54],[15],[28],[51],[80,69],[58,92],[13,12],[91,56],[83,52],[8,48],[62],[54],[25],[36,4],[67,68],[83,36],[47,58],[82],[36],[30,85],[33,87],[42,18],[68,83],[50,53],[32,78],[48,90],[97,95],[13,8],[15,7],[5],[42],[20],[65],[57,9],[2,41],[6],[33],[16,44],[95,30]]
    expected = [null,null,null,null,null,-1,null,null,-1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,90,null,-1,null,null,40,null,null,null,null,null,29,null,null,null,null,17,null,null,null,null,null,null,null,null,null,33,null,null,null,null,null,null,18,null,null,-1,null,null,-1,35,null,null,null,null,null,null,null,-1,-1,null,null,null,null,null,-1,null,null,null,null,null,null,null,null,null,null,null,null,null,-1,null,null,null,null,87,null,null]

    hashMap = MyHashMap()
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        assert getattr(hashMap, m)(*a) == e
