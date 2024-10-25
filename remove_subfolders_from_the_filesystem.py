"""
LeetCode
1233. Remove Sub-Folders from the Filesystem
October 2024 Challenge
jramaswami
"""


class TrieNode:
    def __init__(self, value, terminal=''):
        self.value = value
        self.terminal = False
        self.children = dict()


class Trie:
    def __init__(self):
        self.root = TrieNode('/')
        self.soln = []

    def add(self, path):
        tokens = path[1:].split('/')
        curr = self.root
        for t in tokens:
            if t not in curr.children:
                curr.children[t] = TrieNode(t)
            curr = curr.children[t]
        curr.terminal = path

    def solve(self):
        self.soln = []
        self._rec(self.root)
        return self.soln

    def _rec(self, node):
        if node.terminal:
            self.soln.append(node.terminal)
            return
        for child in node.children.values():
            self._rec(child)
        

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        T = Trie()
        for x in folder:
            T.add(x)
        soln = T.solve()
        return soln
