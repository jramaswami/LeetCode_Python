"""
LeetCode
2359. Find Closest Node to Given Two Nodes
January 2023 Challenge
jramaswami
"""


import collections
import math
from typing import *


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        def bfs(root):
            visited = [False for _ in edges]
            distance = [math.inf for _ in edges]
            queue = collections.deque()
            queue.append(root)
            visited[root] = True
            distance[root] = 0
            while queue:
                u = queue.popleft()
                v = edges[u]
                if v >= 0 and not visited[v]:
                    visited[v] = True
                    distance[v] = 1 + distance[u]
                    queue.append(v)
            return distance

        return min(
            (max(d1, d2), i) for i, (d1, d2) in enumerate(zip(bfs(node1), bfs(node2)))
        )[1]


def test_1():
    edges = [2,2,3,-1]
    node1 = 0
    node2 = 1
    expected = 2
    assert Solution().closestMeetingNode(edges, node1, node2) == expected


def test_2():
    edges = [1,2,-1]
    node1 = 0
    node2 = 2
    expected = 2
    assert Solution().closestMeetingNode(edges, node1, node2) == expected


def test_3():
    "WA"
    edges = [5,4,5,4,3,6,-1]
    node1 = 0
    node2 = 1
    expected = -1
    assert Solution().closestMeetingNode(edges, node1, node2) == expected