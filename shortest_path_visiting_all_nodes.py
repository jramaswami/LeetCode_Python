"""
LeetCode :: February 2022 Challenge :: 847. Shortest Path Visiting All Nodes
jramaswami
"""


import collections
import math


class Solution:

    def shortestPathLength(self, graph):

        all_visited = (1 << (len(graph))) - 1
        soln = math.inf
        for root, _ in enumerate(graph):

            queue = collections.deque()
            queue.append((root, 0, 0 | (1 << root)))
            while queue:
                node, dist, visited = queue.popleft()
                if visited == all_visited:
                    soln = min(soln, dist)
                    break
                for neighbor in graph[node]:
                    visited0 = visited | (1 << neighbor)
                    dist0 = dist + 1
                    queue.append((neighbor, dist0, visited0))

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
    expected = 4
    assert Solution().shortestPathLength(graph) == expected
