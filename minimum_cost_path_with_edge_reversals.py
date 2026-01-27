"""
LeetCode
3650. Minimum Cost Path with Edge Reversals
January 2026 Challenge
jramaswami
"""


import collections
import heapq
import math
from typing import List


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # Create graph
        graph = collections.defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w*2))
        # Dijkstra's algorithm
        distance = [math.inf for _ in range(n)]
        processed = [False for _ in range(n)]
        distance[0] = 0
        queue = [(0, 0)]
        while queue:
            _, u = heapq.heappop(queue)
            if u == n-1:
                return distance[n-1]
            if processed[u]:
                continue
            processed[u] = True
            for v, w in graph[u]:
                if distance[v] > distance[u] + w:
                    distance[v] = distance[u] + w
                    heapq.heappush(queue, (distance[v], v))
        return -1
