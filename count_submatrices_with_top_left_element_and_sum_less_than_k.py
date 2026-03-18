"""
LeetCode
3070. Count Submatrices with Top-Left Element and Sum Less Than k
March 2026 Challenge
jramaswami
"""


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        soln = 0
        dp = [[0 for _ in row] for row in grid]
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                dp[r][c] = grid[r][c]
                if r - 1 >= 0:
                    dp[r][c] += dp[r-1][c]
                if c - 1 >= 0:
                    dp[r][c] += dp[r][c-1]
                if r - 1 >= 0 and c - 1 >= 0:
                    dp[r][c] -= dp[r-1][c-1]
                if dp[r][c] <= k:
                    soln += 1
        return soln