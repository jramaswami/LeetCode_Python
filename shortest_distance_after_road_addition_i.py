"""
LeetCode
3243. Shortest Distance After Road Addition Queries I
November 2024 Challenge
jramaswami
"""


import collections
import heapq
import math


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:        
        def dijkstra(graph, origin, target):
            queue = [(0, origin)]
            dist = collections.defaultdict(lambda: math.inf)
            dist[origin] = 0
            while queue:
                d, u = heapq.heappop(queue)
                if d == dist[u]:
                    if u == target:
                        return d
                    for v in graph[u]:
                        if d + 1 < dist[v]:
                            dist[v] = d + 1
                            heapq.heappush(queue, (d+1, v))
        
        graph = collections.defaultdict(list)
        for u in range(n-1):
            graph[u].append(u+1)
        soln = []
        for u, v in queries:
            graph[u].append(v)
            soln.append(dijkstra(graph, 0, n-1))
        return soln
