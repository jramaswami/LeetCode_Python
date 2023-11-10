"""
LeetCode
1743. Restore the Array From Adjacent Pairs
November 2023 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        degree = collections.defaultdict(int)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        root = [u for u in degree if degree[u] == 1][0]
        visited = set([root])
        soln = [root]
        while len(soln) < len(graph):
            u = soln[-1]
            for v in graph[u]:
                if v not in visited:
                    soln.append(v)
                    visited.add(v)
        return soln


def test_1():
    adjacentPairs = [[2,1],[3,4],[3,2]]
    expected = [1,2,3,4]
    assert Solution().restoreArray(adjacentPairs) == expected


def test_2():
    adjacentPairs = [[2,1],[3,4],[3,2]]
    expected = [1,2,3,4]
    assert Solution().restoreArray(adjacentPairs) == expected


def test_3():
    adjacentPairs = [[2,1],[3,4],[3,2]]
    expected = [1,2,3,4]
    assert Solution().restoreArray(adjacentPairs) == expected