"""
LeetCode
2421. Number of Good Paths
January 2023 Challenge
jramaswami
"""


from typing import *
import collections


class UnionFind:

    def __init__(self, N):
        self.parent = list(range(N))
        self.size = [1 for _ in self.parent]

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

    def connected(self, a, b):
        return self.find(a) == self.find(b)


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:

        # Convert into graph (adjacency list).
        graph = [[] for _ in vals]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        nodes_by_value = collections.defaultdict(list)
        for u, val in enumerate(vals):
            nodes_by_value[val].append(u)

        soln = len(vals)
        uf = UnionFind(len(vals))

        # Process nodes in order by value
        for val in sorted(nodes_by_value):
            # Process all the nodes at this value.
            for u in nodes_by_value[val]:
                # Connect u to any of its adjacent nodes if they have a value
                # less than or equal to the value of u.
                for v in graph[u]:
                    if vals[v] <= val:
                        uf.union(u, v)

            # For each node of this value, how many other nodes *of this value*
            # can the current node connect to.
            count_by_component = collections.defaultdict(int)
            for u in nodes_by_value[val]:
                p = uf.find(u)
                soln += count_by_component[p]
                count_by_component[p] += 1

        return soln




def test_1():
    vals = [1,3,2,1,3]
    edges = [[0,1],[0,2],[2,3],[2,4]]
    expected = 6
    assert Solution().numberOfGoodPaths(vals, edges) == expected


def test_2():
    vals = [1,1,2,2,3]
    edges = [[0,1],[1,2],[2,3],[2,4]]
    expected = 7
    assert Solution().numberOfGoodPaths(vals, edges) == expected


def test_3():
    vals = [1]
    edges = []
    expected = 1
    assert Solution().numberOfGoodPaths(vals, edges) == expected