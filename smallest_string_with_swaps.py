"""
LeetCode :: April 2022 Challenge :: 1202. Smallest String With Swaps
jramaswami
"""


import collections


class UnionFind:
    def __init__(self, n):
        self.id = list(range(n))
        self.size = [1 for _ in range(n)]

    def find(self, u):
        if self.id[u] != u:
            self.id[u] = self.find(self.id[u])
        return self.id[u]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.id[b] = a
            self.size[a] += self.size[b]


class Solution:

    def smallestStringWithSwaps(self, S, pairs):
        uf = UnionFind(len(S))
        for a, b in pairs:
            uf.union(a, b)

        comps = collections.defaultdict(list)
        for i, _ in enumerate(S):
            comps[uf.find(i)].append(i)

        S0 = [' ' for _ in S]
        for i in comps:
            t = sorted(S[j] for j in comps[i])
            u = sorted(comps[i])
            for j, k in enumerate(u):
                S0[k] = t[j]
        return "".join(S0)


def test_1():
    s = "dcab"
    pairs = [[0,3],[1,2]]
    expected = "bacd"
    assert Solution().smallestStringWithSwaps(s, pairs)


def test_2():
    s = "dcab"
    pairs = [[0,3],[1,2],[0,2]]
    expected = "abcd"
    assert Solution().smallestStringWithSwaps(s, pairs)


def test_3():
    s = "cba"
    pairs = [[0,1],[1,2]]
    expected = "abc"
    assert Solution().smallestStringWithSwaps(s, pairs)
