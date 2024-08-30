"""
LeetCode
2699. Modify Graph Edge Weights
August 2024 Challenge
jramaswami

REF: https://algo.monster/liteproblems/2699
"""


import collections
import heapq
from typing import List


INF = pow(10, 10)


def dijkstra(n, graph, source, sink):
    dist = [INF for _ in range(n)]
    dist[source] = 0
    queue = [(0, source)]
    while queue:
        _, u = heapq.heappop(queue)
        if u == sink:
            return dist[u]
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(queue, (dist[u] + w, v))
    return INF


class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        graph = collections.defaultdict(list)
        for u, v, w in edges:
            if w == -1:
                w = INF
            graph[u].append((v, w))
            graph[v].append((u, w))
        # Check the shortest distance initially.
        # If the shortest distance is smaller than target,
        # there is nothing we can do to make it larger.
        # If the shortest distance is the target, then
        # we don't have to do anything.
        d = dijkstra(n, graph, source, destination)
        if d < target:
            return []

        ok = (d == target)
        for edge in edges:
            # Do not modify edges that already have a weight
            if edge[2] > 0:
                continue
            # If we have reached our target distance, change edge to inf
            if ok:
                edge[2] = target
                continue

            # Try setting this edge to 1
            edge[2] = 1
            u, v, w = edge
            graph[u].append((v, 1))
            graph[v].append((u, 1))
            d = dijkstra(n, graph, source, destination)
            if d <= target:
                ok = True
                edge[2] += (target - d)

        if ok:
            return edges
        return []