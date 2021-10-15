"""
LeetCode :: October Challenge :: 309. Best Time to Buy and Sell Stock with Cooldown
jramaswami
"""


import functools


class Solution:

    def maxProfit(self, prices):
        @functools.lru_cache(maxsize=None)
        def max_buy(i):
            # What is the maximum profit I can my if I buy this stock?
            # This will be the maximum profit of any sell that before
            # the index before me.
            if i - 1 > 0:
                return max(max_sell(j) - prices[i] for j in range(0, i - 1))
            elif i >= 0:
                return -prices[i]
            return 0

        @functools.lru_cache(maxsize=None)
        def max_sell(i):
            # What is the maximum profit if I sell a stock here?
            # It will the maximum profit of any buy before me when
            # I sell the stock bought at the current price.
            if i > 0:
                T = max(max_buy(j) + prices[i] for j in range(0, i))
                return max(0, T)
            return 0

        soln = max(max_buy(len(prices) - 1), max_sell(len(prices) - 1))
        return soln


def test_1():
    prices = [1,2,3,0,2]
    expected = 3
    assert Solution().maxProfit(prices) == expected


def test_2():
    prices = [1]
    expected = 0
    assert Solution().maxProfit(prices) == expected
