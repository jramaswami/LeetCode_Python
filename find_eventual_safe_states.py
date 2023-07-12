"""
LeetCode
802. Find Eventual Safe States
July 2023
jramaswami
"""


import collections
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Nodes with outdegree of zero are "safe"
        soln = []
        revgraph = [[] for _ in graph]
        for u, _ in enumerate(graph):
            for v in graph[u]:
                revgraph[v].append(u)
        outdegree = [len(t) for t in graph]
        queue = collections.deque([i for i, t in enumerate(outdegree) if t == 0])
        while queue:
            v = queue.popleft()
            soln.append(v)
            for u in revgraph[v]:
                outdegree[u] -= 1
                if outdegree[u] == 0:
                    queue.append(u)
        soln.sort()
        return soln


def test_1():
    graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    expected = [2,4,5,6]
    assert Solution().eventualSafeNodes(graph) == expected


def test_2():
    graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
    expected = [4]
    assert Solution().eventualSafeNodes(graph) == expected