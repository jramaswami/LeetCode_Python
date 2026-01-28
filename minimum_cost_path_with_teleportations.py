"""
LeetCode
3651. Minimum Cost Path with Teleportations
January 2026 Challenge
jramaswami
"""


import heapq
import math


class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        teleportations = [[set() for _ in row] for row in grid]
        for i, row0 in enumerate(grid):
            for j, _ in enumerate(row0):
                for x, row1 in enumerate(grid):
                    for y, _ in enumerate(row1):
                        if grid[x][y] <= grid[i][j]:
                            teleportations[i][j].add((x, y))

        # distance[number of teleports][row][column] = min distance
        distance = [[[math.inf for _ in row] for row in grid] for _ in range(k+1)]
        processed = [[[False for _ in row] for row in grid] for _ in range(k+1)]
        distance[0][0][0] = 0
        queue = [(0, 0, 0, 0)]
        while queue:
            d, t, r, c = heapq.heappop(queue)
            if processed[t][r][c]:
                continue
            processed[t][r][c] = True
            if r == len(grid)-1 and c == len(grid[0])-1:
                return d

            # Normal moves
            if r + 1 < len(grid):
                r0 = r + 1
                c0 = c
                d0 = d + grid[r0][c0]
                heapq.heappush(queue, (d0, t, r0, c0))
            if c + 1 < len(grid[0]):
                r0 = r
                c0 = c + 1
                d0 = d + grid[r0][c0]
                heapq.heappush(queue, (d0, t, r0, c0))
            # Teleportations
            if t + 1 <= k:
                for r0, c0 in teleportations[r][c]:
                    heapq.heappush(queue, (d, t+1, r0, c0))


def test_1():
    grid = [[1,3,3],[2,5,4],[4,3,5]]
    k = 2
    expected = 7
    assert Solution().minCost(grid, k) == expected