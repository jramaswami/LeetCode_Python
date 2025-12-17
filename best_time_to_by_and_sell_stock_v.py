"""
LeetCode
3573. Best Time to Buy and Sell Stock V
December 2025 Challenge
jramaswami
"""


import functools
import math
from typing import List


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        # dp[day][transactions] = the maximum profit at day i with t transactions
        dp = [[-math.inf for _ in range(k+1)] for _ in range(len(prices) + 1)]
        dp[0][0] = 0
        for i in range(len(prices)):
            for t in range(k+1):
                # No tx
                dp[i+1][t] = max(dp[i+1][t], dp[i][t])
                if t + 1 <= k:
                    # If I have transactions, tx starts on day i and ends on day j
                    # that means I cannot sell before day j + 1
                    for j in range(i+1, len(prices)):
                        # Short tx
                        dp[j+1][t+1] = max(dp[j+1][t+1], prices[i] - prices[j] + dp[i][t])
                        # Normal tx
                        dp[j+1][t+1] = max(dp[j+1][t+1], prices[j] - prices[i] + dp[i][t])
        return max(dp[-1])