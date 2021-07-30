"""
LeetCode :: July 2021 Challenge :: Map Sum Pairs
jramaswami
"""


import string


class TrieNode:
    """Node in a Trie."""
    def __init__(self):
        self.sum = 0
        self.next = dict()
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
        if index >= len(key):
            return None

        if node is None:
            node = TrieNode()

        node.sum += val
        node.next[key[index]] = self._insert(node.next[key[index]], index + 1, key, val)
        return node

    def  sum(self, prefix):
        """Return the sum of vals for any key with the given prefix."""
        return self._sum(self.root, 0, prefix)

    def _sum(self, node, index, prefix):
        """Internal method to return sum of all keys with the given prefix."""
        if node is None:
            return 0

        if index + 1 >= len(prefix):
            return node.sum

        return self._sum(node.next[prefix[index]], index + 1, prefix)



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
