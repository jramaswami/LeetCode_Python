"""
LeetCode
3559. Number of Ways to Assign Edge Weights II
June 2026 Challenge
jramaswami
"""


import collections
import functools
from typing import List


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Build graph
        n = 0
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            n = max(n, u)
            n = max(n, v)

        # Build LCA table
        LEVEL, PARENT = 0, 1
        lca_table = dict()
        queue = collections.deque()
        lca_table[1] = (0, -1)
        queue.append(1)
        while queue:
            u = queue.popleft()
            lvl = lca_table[u][LEVEL]
            for v in graph[u]:
                if v not in lca_table:
                    lca_table[v] = (lvl+1, u)
                    queue.append(v)

        @functools.cache
        def lca(u, v):
            d = 0
            while lca_table[u][LEVEL] > lca_table[v][LEVEL]:
                d += 1
                u = lca_table[u][PARENT]
            while lca_table[v][LEVEL] > lca_table[u][LEVEL]:
                d += 1
                v = lca_table[v][PARENT]
            # u and v are at same level
            while u != v:
                d += 2
                u = lca_table[u][PARENT]
                v = lca_table[v][PARENT]
            return d

        def answer(d):
            if d == 0:
                return 0
            return pow(2, d-1, pow(10,9)+7)

        soln = [answer(lca(u, v)) for u, v in queries]
        return soln