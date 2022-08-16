"""
LeetCode :: 839. Similar String Groups
jramaswami
"""


from typing import *


class UnionFind:

    def __init__(self, N):
        self.size = [1 for _ in range(N)]
        self.ids = [i for i in range(N)]
        self.length = N

    def find(self, u):
        if self.ids[u] != u:
            self.ids[u] = self.find(self.ids[u])
        return self.ids[u]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.ids[b] = a
            self.size[a] += self.size[b]
            self.length -= 1

    def __len__(self):
        return self.length

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        def delta(s1, s2):
            "Return the number of letters out of place in s1."
            return sum(0 if s1[i] == s2[i] else 1 for i, _ in enumerate(s1))

        uf = UnionFind(len(strs))
        for i, s1 in enumerate(strs):
            for j, s2 in enumerate(strs[i+1:], start=i+1):
                d = delta(s1, s2)
                if d == 0 or d == 2:
                    uf.union(i, j)

        return len(uf)


def test_1():
    strs = ["tars","rats","arts","star"]
    expected = 2
    assert Solution().numSimilarGroups(strs) == expected

def test_2():
    strs = ["omv","ovm"]
    expected = 1
    assert Solution().numSimilarGroups(strs) == expected