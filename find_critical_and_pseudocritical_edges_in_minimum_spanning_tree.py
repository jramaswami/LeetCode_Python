"""
LeetCode
1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
August 2023 Challenge
jramaswami
"""


import math
import operator
from typing import List


class UnionFind:

    def __init__(self, n):
        self.id = list(range(n))
        self.size = [1 for _ in self.id]
        self.count = n

    def find(self, x):
        if self.id[x] != x:
            self.id[x] = self.find(self.id[x])
        return self.id[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.id[b] = a
            self.size[a] += self.size[b]
            self.count -= 1


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Sort edges by
        edges = sorted(((a, b, w, i) for i, [a, b, w] in enumerate(edges)), key=operator.itemgetter(2))

        def kruskal(skip_edge_index, uf):
            """
            Kruskal's algorithm
            skip_edge_index: edge_index to skip
            uf: UnionFind passed in so we can force inclusion of an edge
            """
            mst_weight = 0
            for a, b, w, edge_index in edges:
                if uf.find(a) != uf.find(b):
                    if edge_index != skip_edge_index:
                        uf.union(a, b)
                        mst_weight += w

            if uf.count == 1:
                return mst_weight
            return math.inf

        # Get mst weight with all edges
        mst_weight = kruskal(-1, UnionFind(n))
        critical_edges = []
        pseudocritical_edges = []
        for a, b, w, edge_index in edges:
            # First see if deleting this edge causes the mst weight to increase
            mst_weight0 = kruskal(edge_index, UnionFind(n))

            # Now see if we can create a mst with the same weight with the
            # inclusion of this edge
            uf = UnionFind(n)
            uf.union(a, b)
            mst_weight1 = w + kruskal(edge_index, uf)

            if mst_weight0 > mst_weight:
                critical_edges.append(edge_index)
            elif mst_weight1 == mst_weight:
                pseudocritical_edges.append(edge_index)

        return [critical_edges, pseudocritical_edges]


def test_1():
    n = 5
    edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
    expected = [[0,1],[2,3,4,5]]
    result = [sorted(t) for t in Solution().findCriticalAndPseudoCriticalEdges(n, edges)]
    assert result == expected


def test_2():
    n = 4
    edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
    expected = [[],[0,1,2,3]]
    result = [sorted(t) for t in Solution().findCriticalAndPseudoCriticalEdges(n, edges)]
    assert result == expected


def test_3():
    "WA"
    n = 6
    edges = [[0,1,1],[1,2,1],[0,2,1],[2,3,4],[3,4,2],[3,5,2],[4,5,2]]
    expected = [[3],[0,1,2,4,5,6]]
    result = [sorted(t) for t in Solution().findCriticalAndPseudoCriticalEdges(n, edges)]
    assert result == expected


def test_4():
    "WA"
    n = 4
    edges = [[0,1,1],[0,3,1],[0,2,1],[1,2,1],[1,3,1],[2,3,1]]
    expected = [[],[0,1,2,3,4,5]]
    result = [sorted(t) for t in Solution().findCriticalAndPseudoCriticalEdges(n, edges)]
    assert result == expected