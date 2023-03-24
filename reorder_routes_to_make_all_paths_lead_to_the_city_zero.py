"""
LeetCode
1466. Reorder Routes to Make All Paths Lead to the City Zero
March 2023 Challenge
jramaswami
"""


import collections
from typing import *


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))

        visited = [False for _ in graph]
        visited[0] = True
        queue = collections.deque([0])
        cost = 0
        while queue:
            u = queue.popleft()
            for v, c in graph[u]:
                if not visited[v]:
                    cost += c
                    visited[v] = True
                    queue.append(v)
        return cost


