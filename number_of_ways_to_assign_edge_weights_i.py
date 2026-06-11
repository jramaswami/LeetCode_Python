"""
LeetCode
3558. Number of Ways to Assign Edge Weights I
June 2026 Challenge
jramaswami
"""


import math
import collections
from typing import List


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        # There have to be an odd number of 1s on the path

        n = 0
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            n = max(n, u)
            n = max(n, v)

        max_dist = 0
        queue = collections.deque([(1, 0)])
        visited = set()
        visited.add(1)
        while queue:
            u, d = queue.popleft()
            max_dist = max(max_dist, d)
            for v in graph[u]:
                if v not in visited:
                    visited.add(v)
                    queue.append((v, d+1))

        return pow(2, max_dist-1, pow(10,9)+7)