"""
LeetCode
2316. Count Unreachable Pairs of Nodes in an Undirected Graph
March 2023 Challenge
jramaswami
"""


from typing import *
import collections


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False for _ in graph]
        soln = 0
        for root in range(n):
            if not visited[root]:
                component_size = 1
                visited[root] = True
                queue = collections.deque([root])
                while queue:
                    u = queue.popleft()
                    for v in graph[u]:
                        if not visited[v]:
                            component_size += 1
                            visited[v] = True
                            queue.append(v)
                # The nodes in this component cannot reach nodes not in this
                # component
                soln += (component_size * (n - component_size))
        # Divide by two because we have double counted
        return soln // 2


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