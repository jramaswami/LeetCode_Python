"""
LeetCode :: September 2022 Challenge :: 990. Satisfiability of Equality Equations
jramaswami
"""


from typing import *
import string


class UnionFind:

    def __init__(self):
        self.parent = {c: c for c in string.ascii_lowercase}
        self.size = {c: 1 for c in string.ascii_lowercase}

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.parent[b] = a
            self.size[a] += self.size[b]

    def are_equal(self, a, b):
        return self.find(a) == self.find(b)


class Solution:

    def equationsPossible(self, equations: List[str]) -> bool:
        equals = [eqn for eqn in equations if eqn[1:3] == '==']
        not_equals = [eqn for eqn in equations if eqn[1:3] == '!=']

        uf = UnionFind()
        for eqn in equals:
            x, y = eqn[0], eqn[-1]
            uf.union(x, y)

        for eqn in not_equals:
            x, y = eqn[0], eqn[-1]
            if uf.are_equal(x, y):
                return False
        return True


def test_1():
     equations = ["a==b","b!=a"]
     expected = False
     assert Solution().equationsPossible(equations) == expected


def test_2():
    equations = ["b==a","a==b"]
    expected = True
    assert Solution().equationsPossible(equations) == expected