"""
LeetCode
1594. Maximum Non Negative Product in a Matrix
March 2026 Challenge
jramaswami
"""


import math


class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:
        MIN, MAX = 0, 1
        dp = [[[math.inf, -math.inf] for _ in row] for row in grid]
        for r, row in enumerate(grid):
            for c, x in enumerate(row):
                if r == 0 and c == 0:
                    dp[r][c][MIN] = dp[r][c][MAX] = x
                if r - 1 >= 0:
                    for a in (MIN, MAX):
                        dp[r][c][MIN] = min(dp[r][c][MIN], x * dp[r-1][c][a])
                        dp[r][c][MAX] = max(dp[r][c][MAX], x * dp[r-1][c][a])
                if c - 1 >= 0:
                    for a in (MIN, MAX):
                        dp[r][c][MIN] = min(dp[r][c][MIN], x * dp[r][c-1][a])
                        dp[r][c][MAX] = max(dp[r][c][MAX], x * dp[r][c-1][a])
        if dp[-1][-1][MAX] < 0:
            return -1
        return dp[-1][-1][MAX] % (pow(10, 9) + 7)