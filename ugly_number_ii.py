"""
LeetCode
264. Ugly Number II
August 2024 Challenge
jramaswami
"""


import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        visited = set()
        visited.add(1)
        for _ in range(n):
            x = heapq.heappop(heap)
            for m in (2, 3, 5,):
                y = x * m
                if y not in visited:
                    heapq.heappush(heap, y)
                    visited.add(y)
        return x
