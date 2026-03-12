"""
LeetCode
3600. Maximize Spanning Tree Stability with Upgrades
March 2026 Challenge
jramaswami

Thank You Larry!
"""


import itertools


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.id = list(range(n))

    def find(self, u):
        if self.id[u] != u:
            self.id[u] = self.find(self.id[u])
        return self.id[u]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            self.id[a] = b
            return True
        return False


class Solution:
    def maxStability(self, N: int, edges: list[list[int]], k: int) -> int:
        used = 0
        uf = UnionFind(N)
        weights = []

        def add(u, v, strength):
            nonlocal used
            if uf.union(u, v):
                used += 1
                return True
            return False


        consider = []
        for u, v, strength, must in edges:
            if must:
                if not add(u, v, strength):
                    return -1
                weights.append(strength)
            else:
                consider.append((u, v, strength))

        consider.sort(key=lambda x: -x[2])
        upgrade_weights = []
        for u, v, strength in consider:
            if add(u, v, strength):
                upgrade_weights.append(strength)

        upgrade_weights.sort()
        for i in range(min(len(upgrade_weights), k)):
            upgrade_weights[i] *= 2

        assert used < N
        if used == N - 1:
            return min(itertools.chain(weights, upgrade_weights))
        return -1