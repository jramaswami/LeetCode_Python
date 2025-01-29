"""
LeetCode
684. Redundant Connection
January 2025 Challenge
jramaswami
"""


from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.size = [1 for _ in self.parent]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.size[a] += self.size[b]
            self.parent[b] = a
        

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        uf = UnionFind(N)
        for u, v in edges:
            if uf.find(u) == uf.find(v):
                # This is a superfluous edge
                return [u, v]
            uf.union(u, v)
