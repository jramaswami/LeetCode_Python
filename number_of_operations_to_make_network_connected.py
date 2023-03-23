"""
LeetCode
1319. Number of Operations to Make Network Connected
jramaswami
"""


import collections
from typing import *


class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v
        self.used = False

    def other(self, x):
        if x == self.u:
            return self.v
        return self.u


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in connections:
            e = Edge(u, v)
            graph[u].append(e)
            graph[v].append(e)

        visited = [False for _ in range(n)]
        components = 0
        unused_edges = len(connections)
        for root in range(n):
            if not visited[root]:
                components += 1
                queue = collections.deque([root])
                visited[root] = True
                while queue:
                    u = queue.popleft()
                    for e in graph[u]:
                        v = e.other(u)
                        if not visited[v]:
                            e.used = True
                            unused_edges -= 1
                            visited[v] = True
                            queue.append(v)

        # In order to connect x components, you need x - 1 edges.
        if unused_edges >= components - 1:
            return components - 1
        return -1


def test_1():
    n = 4
    connections = [[0,1],[0,2],[1,2]]
    expected = 1
    assert Solution().makeConnected(n, connections) == expected


def test_2():
    n = 6
    connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
    expected = 2
    assert Solution().makeConnected(n, connections) == expected


def test_3():
    n = 6
    connections = [[0,1],[0,2],[0,3],[1,2]]
    expected = -1
    assert Solution().makeConnected(n, connections) == expected