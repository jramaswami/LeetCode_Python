"""
LeetCode :: April 2022 Challenge :: 1584. Min Cost to Connect All Points
jramaswami
"""


class UnionFind:

    def __init__(self, n):
        self.n = n
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
            if self.size[b] > self.size[a]:
                a, b = b, a
            self.id[b] = a
            self.size[a] += self.size[b]

    def are_connected(self, a, b):
        return self.find(a) == self.find(b)


class Solution:

    def minCostConnectPoints(self, points):
        edges = []
        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points[i+1:], start=i+1):
                d = abs(x1 - x2) + abs(y1 - y2)
                edges.append((d, i, j))
        edges.sort()
        uf = UnionFind(len(points))
        soln = 0
        for d, i, j in edges:
            if not uf.are_connected(i, j):
                uf.union(i, j)
                soln += d
        return soln


def test_1():
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    expected = 20
    assert Solution().minCostConnectPoints(points) == expected


def test_2():
    points = [[3,12],[-2,5],[-4,1]]
    expected = 18
    assert Solution().minCostConnectPoints(points) == expected
