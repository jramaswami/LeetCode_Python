"""
LeetCode :: October 2021 Challenge :: 123. Best Time to Buy and Sell Stock III
jramaswami
"""


import functools


class Solution:

    def maxProfit(self, prices):

        @functools.lru_cache(maxsize=None)
        def buy1(i):
            """It's possible to buy the first stock at day i."""
            # Base case.
            if i >= len(prices):
                return 0
            # You can choose to buy first stock on day i and then sell later,
            # sell(i+1) - prices[i] or you can choose to buy later, buy(i+1).
            return max(sell1(i+1) - prices[i], buy1(i+1))

        @functools.lru_cache(maxsize=None)
        def sell1(i):
            """Holding first stock, it's possible to sell on day i."""
            # Base case.
            if i >= len(prices):
                return 0
            # You can choose to sell the stock being held on day i and then
            # buy stock 2 later, prices[i] + buy2(i+1), or you can choose
            # to sell the stock being held later, sell1(i+1).
            return max(prices[i] + buy2(i+1), sell1(i+1))

        @functools.lru_cache(maxsize=None)
        def buy2(i):
            """It's possible to buy the second stock at day i."""
            # Base case.
            if i >= len(prices):
                return 0
            # You can choose to buy second stock on day i and then sell later,
            # sell(i+1) - prices[i] or you can choose to buy later, buy(i+1).
            return max(sell2(i+1) - prices[i], buy2(i+1))

        @functools.lru_cache(maxsize=None)
        def sell2(i):
            """Holding second stock, it's possible to sell on day i."""
            # Base case.
            if i >= len(prices):
                return 0
            # You can choose to sell the stock being held on day i, prices[i],
            # or you can choose to sell the stock being held later, sell2(i+1).
            return max(prices[i], sell2(i+1))

        return buy1(0)


def test_1():
    prices = [3,3,5,0,0,3,1,4]
    expected = 6
    assert Solution().maxProfit(prices) == expected


def test_2():
    prices = [1,2,3,4,5]
    expected = 4
    assert Solution().maxProfit(prices) == expected


def test_3():
    prices = [7, 6, 4, 3, 1]
    expected = 0
    assert Solution().maxProfit(prices) == expected


def test_4():
    prices = [1]
    expected = 0
    assert Solution().maxProfit(prices) == expected
