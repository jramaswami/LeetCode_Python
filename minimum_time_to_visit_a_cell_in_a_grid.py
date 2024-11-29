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

        def inbounds(r, c):
            return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[r])

        def neighbors(r, c):
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        # Make sure that you can leave the origin
        if all(grid[r0][c0] > 1 for r0, c0 in neighbors(0, 0)):
            return -1

        # Because we can backtrack once we have two cells we can visit,
        # we can jitter back and forth until we can move to an unvisited
        # cell.  This means that the parity of the current cells visit time
        # determines when we can visit an adjacent cell.
        max_time = [[math.inf for _ in row] for row in grid]
        queue = []
        heapq.heappush(queue, (0, 0, 0))
        max_time[0][0] = 0
        while queue:
            t, r, c = heapq.heappop(queue)
            if t == max_time[r][c]:
                if r == len(grid) - 1 and c == len(grid[0]) - 1:
                    return t
                for r0, c0 in neighbors(r, c):
                    if grid[r0][c0] > t:
                        curr_cell_parity = t % 2
                        neighbor_cell_parity = grid[r0][c0] % 2
                        t0 = grid[r0][c0]
                        if curr_cell_parity == neighbor_cell_parity:
                            t0 = grid[r0][c0] + 1
                    else:
                        t0 = t + 1
                    if t0 < max_time[r0][c0]:
                        max_time[r0][c0] = t0
                        heapq.heappush(queue, (t0, r0, c0))