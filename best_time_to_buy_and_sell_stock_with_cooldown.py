"""
LeetCode
309. Best Time to Buy and Sell Stock with Cooldown
December 2022 Challenge
jramaswami
"""


import functools


class Solution:

    def maxProfit(self, prices):

        @functools.cache
        def buy(i):
            if i >= len(prices):
                return 0

            return max(
                sell(i+1) - prices[i],
                buy(i+1)
            )

        @functools.cache
        def sell(i):
            if i >= len(prices):
                return 0
            return max(
                prices[i] + buy(i+2),
                sell(i+1)
            )

        return buy(0)


def test_1():
    prices = [1,2,3,0,2]
    expected = 3
    assert Solution().maxProfit(prices) == expected


def test_2():
    prices = [1]
    expected = 0
    assert Solution().maxProfit(prices) == expected
