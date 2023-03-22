"""
LeetCode
2492. Minimum Score of a Path Between Two Cities
March 2023 Challenge
jramaswami
"""


import collections
import math
from typing import *


class Edge:
    def __init__(self, u, v, wt):
        self.u = u
        self.v = v
        self.wt = wt
        self.used = False

    def other(self, x):
        if x == self.u:
            return self.v
        return self.u

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n+1)]
        for a, b, wt in roads:
            e = Edge(a, b, wt)
            graph[a].append(e)
            graph[b].append(e)

        soln = math.inf
        queue = collections.deque([1])
        while queue:
            u = queue.popleft()
            for e in graph[u]:
                if not e.used:
                    soln = min(e.wt, soln)
                    e.used = True
                    queue.append(e.other(u))
        return soln


def test_1():
    n = 4
    roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
    expected = 5
    assert Solution().minScore(n, roads) == expected


def test_2():
    n = 4
    roads = [[1,2,2],[1,3,4],[3,4,7]]
    expected = 2
    assert Solution().minScore(n, roads) == expected