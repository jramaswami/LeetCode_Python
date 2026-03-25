"""
LeetCode
3546. Equal Sum Grid Partition I
March 2026 Challenge
jramaswami
"""


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = 0
        dp = [[0 for _ in row] for row in grid]
        for r, row in enumerate(grid):
            for c, x in enumerate(row):
                total += x
                dp[r][c] = x
                if r-1 >= 0:
                    dp[r][c] += dp[r-1][c]
                if c-1 >= 0:
                    dp[r][c] += dp[r][c-1]
                if r-1 >= 0 and c-1 >= 0:
                    dp[r][c] -= dp[r-1][c-1]

        # Horizontal cuts
        R, C = len(grid), len(grid[0])
        for r in range(R-1):
            x = dp[r][C-1]
            if total - x == x:
                return True
        # Vertical cuts
        for c in range(C-1):
            x = dp[R-1][c]
            if total - x == x:
                return True
        return False