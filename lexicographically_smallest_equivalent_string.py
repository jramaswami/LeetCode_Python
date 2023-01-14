"""
LeetCode
1061. Lexicographically Smallest Equivalent String
January 2023 Challenge
jramaswami
"""


import string
from typing import *


class UnionFind:

    def __init__(self):
        self.parent = {c: c for c in string.ascii_lowercase}

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if b < a:
            a, b = b, a
        self.parent[b] = a


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind()
        for a, b in zip(s1, s2):
            uf.union(a, b)

        return "".join(uf.find(c) for c in baseStr)


def test_1():
    s1 = "parker"
    s2 = "morris"
    baseStr = "parser"
    expected = "makkek"
    assert Solution().smallestEquivalentString(s1, s2, baseStr) == expected


def test_2():
    s1 = "hello"
    s2 = "world"
    baseStr = "hold"
    expected = "hdld"
    assert Solution().smallestEquivalentString(s1, s2, baseStr) == expected


def test_3():
    s1 = "leetcode"
    s2 = "programs"
    baseStr = "sourcecode"
    expected = "aauaaaaada"
    assert Solution().smallestEquivalentString(s1, s2, baseStr) == expected