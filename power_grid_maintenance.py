"""
LeetCode
3607. Power Grid Maintenance
November 2025 Challenge
jramaswami
"""


import collections
import sortedcontainers
from typing import List


class UnionFind:
    def __init__(self, n):
        self.id = [x for x in range(n+1)]
        self.size = [1 for x in range(n+1)]
        self.size[0] = 0

    def find(self, a):
        if self.id[a] != a:
            self.id[a] = self.find(self.id[a])
        return self.id[a]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.size[a] += self.size[b]
            self.id[b] = a


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        uf = UnionFind(c)
        online = [True for _ in range(c+1)]
        online[0] = False
        for u, v in connections:
            uf.union(u, v)
        minstation = collections.defaultdict(sortedcontainers.SortedList)
        for station in range(1, c+1):
            grid = uf.find(station)
            minstation[grid].add(station)

        soln = []
        for operation, station in queries:
            if operation == 1:
                if online[station]:
                    soln.append(station)
                else:
                    grid = uf.find(station)
                    if minstation[grid]:
                        soln.append(minstation[grid][0])
                    else:
                        soln.append(-1)
            else:
                if online[station]:
                    online[station] = False
                    grid = uf.find(station)
                    minstation[grid].remove(station)
        return soln