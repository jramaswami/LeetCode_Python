"""
LeetCode :: February 2022 Challenge :: 847. Shortest Path Visiting All Nodes
jramaswami

Thank You Larry!
"""


import itertools
import math
import functools


class Solution:

    def shortestPathLength(self, graph):

        # Floyd-Warshall: shortest distance between all pairs.
        dist = [[math.inf for _ in graph] for _ in graph]
        for node, neighbors in enumerate(graph):
            dist[node][node] = 0
            for neighbor in neighbors:
                dist[node][neighbor] = 1

        for k in range(len(graph)):
            for i in range(len(graph)):
                for j in range(len(graph)):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        @functools.cache
        def visit(node, visited):
            if visited == (1 << len(graph)) - 1:
                return 0

            result = math.inf
            for i, _ in enumerate(graph):
                mask = 1 << i
                if not (visited & mask):
                    result = min(result, visit(i, mask | visited) + dist[node][i])
            return result

        soln = math.inf
        for root, _ in enumerate(graph):
            soln = min(soln, visit(root, 1 << root))
        return soln


def test_1():
    graph = [[1,2,3],[0],[0],[0]]
    expected = 4
    assert Solution().shortestPathLength(graph) == expected


def test_2():
    graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
    expected = 4
    assert Solution().shortestPathLength(graph) == expected


def test_3():
    "Complete graph."
    graph = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11], [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11], [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11], [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11], [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11], [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11], [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11], [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    expected = 11
    assert Solution().shortestPathLength(graph) == expected
