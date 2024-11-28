"""
LeetCode
2290. Minimum Obstacle Removal to Reach Corner
November 2024 Challenge
jramaswami
"""


import heapq
import math
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        dist = [[math.inf for _ in row] for row in grid]
        dist[0][0] = grid[0][0]
        queue = []
        heapq.heappush(queue, (grid[0][0], 0, 0))
        while queue:
            d, r, c = heapq.heappop(queue)
            if d == dist[r][c]:
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    r0, c0 = r + dr, c + dc
                    if r0 >= 0 and r0 < len(grid) and c0 >= 0 and c0 < len(grid[r]):
                        if d + grid[r0][c0] < dist[r0][c0]:
                            dist[r0][c0] = d + grid[r0][c0]
                            heapq.heappush(queue, (dist[r0][c0], r0, c0))
        return dist[-1][-1]
