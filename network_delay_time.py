"""
LeetCode :: May 2022 Challenge :: 743. Network Delay Time
jramaswami
"""


import heapq
import math


class Solution:

    def networkDelayTime(self, times, node_count, signal_node):
        adj = [[] for _ in range(node_count+1)]
        for u, v, w in times:
            adj[u].append((v, w))

        dist = [math.inf for _ in adj]
        dist[signal_node] = 0
        queue = [(0, signal_node)]
        while queue:
            d, u = heapq.heappop(queue)
            if dist[u] != d:
                continue
            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(queue, (dist[v], v))

        soln = max(dist[1:])
        return soln if soln < math.inf else -1


def test_1():
    times = [[2,1,1],[2,3,1],[3,4,1]]
    n = 4
    k = 2
    expected = 2
    assert Solution().networkDelayTime(times, n, k) == expected


def test_2():
    times = [[1,2,1]]
    n = 2
    k = 1
    expected = 1
    assert Solution().networkDelayTime(times, n, k) == expected


def test_3():
    times = [[1,2,1]]
    n = 2
    k = 2
    expected = -1
    assert Solution().networkDelayTime(times, n, k) == expected