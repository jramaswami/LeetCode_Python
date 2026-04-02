"""
LeetCode
3418. Maximum Amount of Money Robot Can Earn
April 2026 Challenge
jramaswami
"""


from typing import List
import math


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        # dp[row][col][neutralizations left]
        dp = [[[-math.inf for _ in range(3)] for _ in row] for row in coins]
        dp[0][0][0] = 0
        dp[0][0][1] = 0
        dp[0][0][2] = coins[0][0]

        for r, row in enumerate(coins):
            for c, _ in enumerate(row):
                for n in range(3):
                    # Down
                    if r + 1 < len(coins):
                        # Use neutralization
                        if n > 0:
                            dp[r+1][c][n-1] = max(dp[r+1][c][n-1], dp[r][c][n])
                        # Don't use neutralization
                        dp[r+1][c][n] = max(dp[r+1][c][n], dp[r][c][n] + coins[r+1][c])
                    # Right
                    if c + 1 < len(coins[r]):
                        if n > 0:
                            dp[r][c+1][n-1] = max(dp[r][c+1][n-1], dp[r][c][n])
                        # Don't use neutralization
                        dp[r][c+1][n] = max(dp[r][c+1][n], dp[r][c][n] + coins[r][c+1])
        return max(dp[-1][-1][n] for n in range(3))