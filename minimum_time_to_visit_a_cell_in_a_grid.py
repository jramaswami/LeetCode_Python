"""
LeetCode
2577. Minimum Time to Visit a Cell In a Grid
November 2024 Challenge
jramaswami
"""


import heapq
import math
from typing import List


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        curr_queue = set([(0, 0)])
        next_queue = set()
        curr_time = 0
        for _ in range(pow(10,5)):
            curr_time += 1
            for r, c in curr_queue:
                for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    r0, c0 = r + dr, c + dc
                    if r0 >= 0 and r0 < len(grid) and c0 >= 0 and c0 < len(grid[r]):
                        if curr_time >= grid[r0][c0]:
                            if r0 == N - 1 and c0 == M - 1:
                                return curr_time
                            next_queue.add((r0, c0))
            if not next_queue:
                return -1
            curr_queue, next_queue = next_queue, set()
        return -1