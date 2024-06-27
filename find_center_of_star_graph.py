"""
LeetCode
1791. Find Center of Star Graph
June 2024 Challenge
jramaswami
"""


import collections


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        degree = collections.defaultdict(int)
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
        
        return [t for t in degree if degree[t] == len(degree) - 1][0]
