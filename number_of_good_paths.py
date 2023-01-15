"""
LeetCode
2421. Number of Good Paths
January 2023 Challenge
jramaswami
"""


from typing import *
import collections


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:

        # Convert into graph (adjacency list).
        graph = [[] for _ in vals]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        soln = 0
        for root, max_val in enumerate(vals):
            queue = collections.deque([(root, -1)])
            while queue:
                u, p = queue.popleft()
                if vals[u] == vals[root] and u <= root:
                    soln += 1
                for v in graph[u]:
                    if v != p and vals[v] <= max_val:
                        queue.append((v, u))
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