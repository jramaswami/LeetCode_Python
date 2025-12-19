"""
LeetCode
2092. Find All People With Secret
December 2025 Challenge
jramaswami
"""


import collections
from typing import List


class AugmentedUnionFind:
    def __init__(self):
        self.parent = dict()
        self.size = dict()
        self.knows_secret = dict()

    def add(self, x, knows):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1
            self.knows_secret[x] = knows

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            self.knows_secret[x] |= self.parent[x]
            return self.parent[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.parent[b] = a
            self.knows_secret[a] |= self.knows_secret[b]
            self.size[a] += self.size[b]


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        knows_secret = set()
        # Person 0 shares with firstPerson at time 0
        knows_secret.add(0)
        knows_secret.add(firstPerson)

        meetings_by_time = collections.defaultdict(list)
        for x, y, t in meetings:
            meetings_by_time[t].append((x, y))

        for t in sorted(meetings_by_time):
            # Augmented union find with knows secret.
            uf = AugmentedUnionFind()
            for x, y in meetings_by_time[t]:
                uf.add(x, x in knows_secret)
                uf.add(y, y in knows_secret)
                uf.union(x, y)

            # Record if they know the secret
            for x, y in meetings_by_time[t]:
                z = uf.find(x)
                if uf.knows_secret[z]:
                    knows_secret.add(x)
                z = uf.find(y)
                if uf.knows_secret[z]:
                    knows_secret.add(y)
        return list(knows_secret)