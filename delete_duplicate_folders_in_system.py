"""
LeetCode
1948. Delete Duplicate Folders in System
July 2025 Challenge
jramaswami

REF: https://leetcode.doocs.org/en/lc/1948/#solution-1-trie-dfs
"""


import collections
from typing import List


class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.deleted = False


class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Trie()
        for path in paths:
            curr = root
            for name in path:
                if curr.children[name] is None:
                    curr.children[name] = Trie()
                curr = curr.children[name]

        g = {}

        def dfs(node):
            if not node.children:
                return ""
            subs = []
            for name, child in node.children.items():
                subs.append(f"{name}({dfs(child)})")
            s = "".join(sorted(subs))
            if s in g:
                node.deleted = g[s].deleted = True
            else:
                g[s] = node
            return s

        def dfs2(node):
            if node.deleted:
                return
            if path:
                ans.append(path[:])
            for name, child in node.children.items():
                path.append(name)
                dfs2(child)
                path.pop()

        dfs(root)
        ans = []
        path = []
        dfs2(root)
        return ans


def test_1():
    paths = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]
    expected = [["d"],["d","a"]]
    assert Solution().deleteDuplicateFolder(paths) == expected