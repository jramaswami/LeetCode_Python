"""
LeetCode
3651. Minimum Cost Path with Teleportations
January 2026 Challenge
jramaswami
"""


import math


class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        # teleporations[row][col] = list of destinations
        teleportations = [[[] for _ in row] for row in grid]
        for i, row0 in enumerate(grid):
            for j, _ in enumerate(row0):
                for x, row1 in enumerate(grid):
                    for y, _ in enumerate(row1):
                        if grid[x][y] <= grid[i][j]:
                            teleportations[i][j].append((x, y))

        # dp[number of teleports][row][column] = min distance
        dp = [[[math.inf for _ in row] for row in grid] for _ in range(k+1)]
        dp[0][0][0] = 0

        for t in range(k+1):
            for r, row in enumerate(grid):
                for c, _ in enumerate(row):
                    # Normal moves
                    if r + 1 < len(grid):
                        dp[t][r+1][c] = min(dp[t][r+1][c], dp[t][r][c] + grid[r+1][c])
                    if c + 1 < len(row):
                        dp[t][r][c+1] = min(dp[t][r][c+1], dp[t][r][c] + grid[r][c+1])
                    # Teleportations
                    if t + 1 <= k:
                        for r0, c0 in teleportations[r][c]:
                            dp[t+1][r0][c0] = min(dp[t+1][r0][c0], dp[t][r][c])

        soln = math.inf
        for t in range(k+1):
            soln = min(soln, dp[t][-1][-1])
        return soln


def test_1():
    grid = [[1,3,3],[2,5,4],[4,3,5]]
    k = 2
    expected = 7
    assert Solution().minCost(grid, k) == expected