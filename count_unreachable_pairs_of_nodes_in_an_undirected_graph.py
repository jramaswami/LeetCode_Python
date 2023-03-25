"""
LeetCode
2316. Count Unreachable Pairs of Nodes in an Undirected Graph
March 2023 Challenge
jramaswami
"""


from typing import *
import collections
import itertools


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False for _ in graph]
        component_sizes = []
        for root in range(n):
            if not visited[root]:
                component_sizes.append(1)
                visited[root] = True
                queue = collections.deque([root])
                while queue:
                    u = queue.popleft()
                    for v in graph[u]:
                        if not visited[v]:
                            component_sizes[-1] += 1
                            visited[v] = True
                            queue.append(v)
        assert sum(component_sizes) == n
        if len(component_sizes) == 1:
            return 0
        return sum((a * b) for a, b in itertools.combinations(component_sizes, 2))


def test_1():
    n = 3
    edges = [[0,1],[0,2],[1,2]]
    expected = 0
    assert Solution().countPairs(n, edges) == expected


def test_2():
    n = 7
    edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
    expected = 14
    assert Solution().countPairs(n, edges) == expected