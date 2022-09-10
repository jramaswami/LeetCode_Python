"""
LeetCode :: September 2022 Challenge :: 188. Best Time to Buy and Sell Stock IV
jramaswami
"""


import functools
from typing import *


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        @functools.cache
        def buy(day, tx):
            # Prune: you cannot buy more than k times.
            if tx == k:
                return 0

            # Base Case.
            if day >= len(prices):
                return 0

            return max (
                # I can buy today
                sell(day+1, tx+1) - prices[day],
                # I can skip today
                buy(day+1, tx)
            )

        @functools.cache
        def sell(day, tx):
            # Base case.
            if day >= len(prices):
                return 0

            return max(
                # I can hold.
                sell(day+1, tx),
                # I can sell today.
                buy(day+1, tx) + prices[day]
            )

        return buy(0, 0)


def test_1():
    k = 2
    prices = [2,4,1]
    expected = 2
    assert Solution().maxProfit(k, prices) == expected


def test_2():
    k = 2
    prices = [3,2,6,5,0,3]
    expected = 7
    assert Solution().maxProfit(k, prices) == expected