"""
LeetCode
2685. Count the Number of Complete Components
March 2025 Challenge
jramaswami

Complete graph has n * (n-1) / 2 edges in it
"""


import collections
from typing import List


class UnionFind:
    def __init__(self, N):
        self.N = N
        self.id = list(range(N))
        self.size = [1 for _ in self.id]

    def parent(self, a):
        if self.id[a] != a:
            self.id[a] = self.parent(self.id[a])
        return self.id[a]

    def union(self, a, b):
        a = self.parent(a)
        b = self.parent(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.size[a] += self.size[b]
            self.id[b] = a


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)

        edge_count = collections.defaultdict(int)
        for u, _ in edges:
            root = uf.parent(u)
            edge_count[root] += 1

        soln = 0
        for root in range(n):
            if uf.parent(root) == root:
                size = uf.size[root]
                edges = edge_count[root]
                expected = (size * (size - 1)) // 2
                if expected == edges:
                    soln += 1
        return soln