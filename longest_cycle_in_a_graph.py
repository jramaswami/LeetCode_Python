"""
LeetCode
2360. Longest Cycle in a Graph
March 2023 Challenge
jramaswami
"""


from typing import *


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = [False for _ in edges]
        soln = -1
        for root, _ in enumerate(edges):
            if not visited[root] and edges[root] >= 0:
                path = {}
                curr = root
                while curr >= 0 and not visited[curr]:
                    visited[curr] = True
                    path[curr] = len(path)
                    curr = edges[curr]
                if curr in path:
                    soln = max(soln, len(path) - path[curr])
        return soln


def test_1():
    edges = [3,3,4,2,3]
    expected = 3
    assert Solution().longestCycle(edges) == expected


def test_2():
    edges = [2,-1,3,1]
    expected = -1
    assert Solution().longestCycle(edges) == expected


def test_3():
    "WA"
    edges = [-1,4,-1,2,0,4]
    expected = -1
    assert Solution().longestCycle(edges) == expected