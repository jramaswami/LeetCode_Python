"""
LeetCode :: July 2021 Challenge :: Map Sum Pairs
jramaswami

REF: Algorithms, Sedwick, pp. 732-738
"""


import string


class TrieNode:
    """Node in a Trie."""
    def __init__(self):
        self.sum = 0
        self.next = dict()
        self.word = None
        for c in string.ascii_lowercase:
            self.next[c] = None


class MapSum:
    """A Trie."""
    def __init__(self):
        """Initialize data structure."""
        self.root = TrieNode()

    def insert(self, key, val):
        """Insert key into datastructure along with value."""
        self._insert(self.root, 0, key, val)

    def _insert(self, node, index, key, val):
        """Internal method to insert key into trie."""
        if node is None:
            node = TrieNode()

        if index == len(key):
            node.word = key
            node.sum = val
            return node

        node.next[key[index]] = self._insert(node.next[key[index]], index + 1, key, val)
        return node

    def  sum(self, prefix):
        """Return the sum of vals for any key with the given prefix."""
        node = self._get(self.root, 0, prefix)
        prefix0 = list(prefix)
        Q = []
        self._collect(node, prefix0, Q)
        return sum(Q)

    def _get(self, node, index, prefix):
        """Get the terminal node for prefix."""
        if node is None:
            return None
        if index == len(prefix):
            return node
        c = prefix[index]
        return self._get(node.next[c], index + 1, prefix)

    def _collect(self, node, prefix, Q):
        """Internal method to return sum of all keys with the given prefix."""
        if node is None:
            return

        if node.word is not None:
            Q.append(node.sum)

        for c in string.ascii_lowercase:
            prefix.append(c)
            self._collect(node.next[c], prefix, Q)
            prefix.pop()


def test_1():
    calls = ["MapSum", "insert", "sum", "insert", "sum"]
    args = [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
    expected = [None, None, 3, None, 5]

    ms = MapSum()
    for c, a, e in zip(calls[1:], args[1:], expected[1:]):
        assert getattr(ms, c)(*a) == e


def test_2():
    """WA"""
    calls = ["MapSum", "insert", "sum", "insert", "sum"]
    args = [[], ["a",3], ["ap"], ["b",2], ["a"]]
    expected = [None,None,0,None,3]
    ms = MapSum()
    for c, a, e in zip(calls[1:], args[1:], expected[1:]):
        assert getattr(ms, c)(*a) == e


def test_3():
    """WA"""
    calls = ["MapSum", "insert", "sum", "insert", "insert", "sum"]
    args = [[], ["apple",3], ["ap"], ["app",2], ["apple", 2], ["ap"]]
    expected = [None,None,3,None,None,4]
    ms = MapSum()
    for c, a, e in zip(calls[1:], args[1:], expected[1:]):
        assert getattr(ms, c)(*a) == e
