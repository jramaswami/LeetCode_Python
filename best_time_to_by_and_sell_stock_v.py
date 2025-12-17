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

        @functools.cache
        def rec(index, state, txs):
            # Base Cases
            # If we have run out of transactions
            if txs == 0:
                return 0
            # If we have run out of days
            if index >= len(prices):
                if state == NONE:
                    return 0
                return -math.inf

            # Recursive Cases
            if state == LONG:
                sell = rec(index+1, NONE, txs-1) + prices[index]
                hold = rec(index+1, LONG, txs)
                return max(sell, hold)
            elif state == SHORT:
                buy = rec(index+1, NONE, txs-1) - prices[index]
                hold = rec(index+1, SHORT, txs)
                return max(buy, hold)
            # NONE
            buy = rec(index+1, LONG, txs) - prices[index]
            sell = rec(index+1, SHORT, txs) + prices[index]
            hold = rec(index+1, NONE, txs)
            return max((buy, sell, hold))

        return rec(0, NONE, k)