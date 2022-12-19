"""
LeetCode
1971. Find if Path Exists in Graph
December 2022 Challenge
jramaswami
"""


from typing import *
import collections


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False for _ in range(n)]
        visited[source] = True
        queue = collections.deque()
        queue.append(source)
        while queue:
            u = queue.popleft()
            if u == destination:
                return True
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
        return False


def test_1():
    n = 3
    edges = [[0,1],[1,2],[2,0]]
    source = 0
    destination = 2
    expected = True
    assert Solution().validPath(n, edges, source, destination) == expected


def test_2():
    n = 6
    edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
    source = 0
    destination = 5
    expected = False
    assert Solution().validPath(n, edges, source, destination) == expected


def test_3():
    "WA"
    n = 10
    edges = [[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]]
    source = 7
    destination = 5
    expected = True
    assert Solution().validPath(n, edges, source, destination) == expected
