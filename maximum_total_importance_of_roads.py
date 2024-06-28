"""
LeetCode
2285. Maximum Total Importance of Roads
June 2024 Challenge
jramaswami
"""


import collections


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = collections.Counter()
        for u, v in roads:
            degree[u] += 1
            degree[v] += 1
        
        soln = 0
        for x, d in zip(range(n, 0, -1), sorted(degree.values(), reverse=True)):
            soln += x * d
        return soln
