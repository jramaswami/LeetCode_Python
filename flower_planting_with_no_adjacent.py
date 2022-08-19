"""
LeetCode :: 1042. Flower Planting With No Adjacent
jramaswami
"""


from typing import *
import collections


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # Convert edges into an adjacency list.
        adj = [[] for _ in range(n+1)]
        for u, v in paths:
            adj[u].append(v)
            adj[v].append(u)

        # Assigne colors using MEX.
        color = [-1 for _ in range(n+1)]
        for u in range(1, n+1):
            color[u] = min(x for x in [1,2,3,4] if x not in (color[v] for v in adj[u]))
        return color[1:]


def test_1():
    n = 3
    paths = [[1,2],[2,3],[3,1]]
    expected = [1,2,3]
    assert Solution().gardenNoAdj(n, paths) == expected