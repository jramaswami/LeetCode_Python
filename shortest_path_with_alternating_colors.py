"""
LeetCode
1129. Shortest Path with Alternating Colors
February 2023 Challenge
jramaswami
"""


from typing import *
import collections
import math


RED, BLUE = 0, 1


Edge = collections.namedtuple('Edge', ['node_v', 'color'])
QItem = collections.namedtuple('Node', ['node_u', 'color'])


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # Convert to adj list
        adj = [[] for _ in range(n)]
        for u, v in redEdges:
            adj[u].append(Edge(v, RED))
        for u, v in blueEdges:
            adj[u].append(Edge(v, BLUE))

        dist = [[math.inf for _ in range(n)] for _ in range(2)]
        dist[RED][0] = dist[BLUE][0] = 0
        queue = collections.deque()
        queue.append(QItem(0, RED))
        queue.append(QItem(0, BLUE))
        while queue:
            node = queue.popleft()
            for edge in adj[node.node_u]:
                if node.color != edge.color:
                    if dist[node.color][node.node_u] + 1 < dist[edge.color][edge.node_v]:
                        dist[edge.color][edge.node_v] = dist[node.color][node.node_u] + 1
                        queue.append(QItem(edge.node_v, edge.color))

        def result(a, b):
            t = min(a, b)
            return t if t < math.inf else -1

        return [result(dist[RED][u], dist[BLUE][u]) for u in range(n)]


def test_1():
    n = 3
    redEdges = [[0,1],[1,2]]
    blueEdges = []
    expected = [0,1,-1]
    assert Solution().shortestAlternatingPaths(n, redEdges, blueEdges) == expected


def test_2():
    n = 3
    redEdges = [[0,1]]
    blueEdges = [[2,1]]
    expected = [0,1,-1]
    assert Solution().shortestAlternatingPaths(n, redEdges, blueEdges) == expected