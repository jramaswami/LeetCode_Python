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
        LONG, SHORT, NONE = 0, 1, 2

        # dp[day index][transactions][state]
        dp = [[[-math.inf for _ in range(3)] for _ in range(k+1)] for _ in range(len(prices) + 1)]
        dp[0][0][NONE] = 0
        for today in range(len(prices)):
            tomorrow = today + 1
            todays_price = prices[today]
            for tx in range(k+1):
                # LONG
                # Selling a stock I am holding
                if tx+ 1 <= k:
                    dp[tomorrow][tx+1][NONE] = max(dp[tomorrow][tx+1][NONE], dp[today][tx][LONG] + todays_price)
                # Holding the stock
                dp[tomorrow][tx][LONG] = max(dp[tomorrow][tx][LONG], dp[today][tx][LONG])
                # SHORT
                # Buying the stock that I shorted
                if tx+ 1 <= k:
                    dp[tomorrow][tx+1][NONE] = max(dp[tomorrow][tx+1][NONE], dp[today][tx][SHORT] - todays_price)
                # Holding the short
                dp[tomorrow][tx][SHORT] = max(dp[tomorrow][tx][SHORT], dp[today][tx][SHORT])
                # NONE
                # Buying a stock to sell later
                dp[tomorrow][tx][LONG] = max(dp[tomorrow][tx][LONG], dp[today][tx][NONE] - todays_price)
                # Selling a stock to short later
                dp[tomorrow][tx][SHORT] = max(dp[tomorrow][tx][SHORT], dp[today][tx][NONE] + todays_price)
                # Not buying or selling
                dp[tomorrow][tx][NONE] = max(dp[tomorrow][tx][NONE], dp[today][tx][NONE])

        soln = -math.inf
        for j in range(k+1):
            soln = max(dp[-1][j][NONE], soln)
        return soln