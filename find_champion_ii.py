"""
LeetCode
2924. Find Champion II
November 2024 Challenge
jramaswami
"""


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0 for _ in range(n)]
        for u, v in edges:
            indegree[v] += 1
        champions = [i for i, x in enumerate(indegree) if x == 0]
        if len(champions) == 1:
            return champions[0]
        return -1