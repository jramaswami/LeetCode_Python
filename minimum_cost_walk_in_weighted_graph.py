"""
LeetCode
3108. Minimum Cost Walk in Weighted Graph
March 2025 Challenge
jramaswami

Thank You NeetCode.IO!
"""


class UnionFind:
    def __init__(self, N):
        self.N = N
        self.id = list(range(N))
        x = pow(2, 32) - 1
        assert pow(10,5) <= x
        self.weight = [x for _ in range(N)]
        self.size = [1 for _ in range(N)]

    def parent(self, a):
        if self.id[a] != a:
            self.id[a] = self.parent(self.id[a])
        return self.id[a]

    def union(self, a, b, w):
        a = self.parent(a)
        b = self.parent(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.size[a] += self.size[b]
            self.id[b] = a
        self.weight[a] = self.weight[a] & self.weight[b] & w

    def query(self, a, b):
        a = self.parent(a)
        b = self.parent(b)
        if a == b:
            return self.weight[a]
        return -1


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        uf = UnionFind(n)
        for u, v, w in edges:
            uf.union(u, v, w)
        return [uf.query(u, v) for u, v in query]