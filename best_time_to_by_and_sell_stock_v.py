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
        @functools.cache
        def rec(i, t):
            if i >= len(prices):
                return 0

            if t >= k:
                return 0

            # Normal tx
            result = -math.inf
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                result = max(result, profit + rec(j+1, t+1))
            # Short tx
            for j in range(i+1, len(prices)):
                profit = prices[i] - prices[j]
                result = max(result, profit + rec(j+1, t+1))
            # No tx
            result = max(result, rec(i+1, t))
            return result

        return rec(0, 0)