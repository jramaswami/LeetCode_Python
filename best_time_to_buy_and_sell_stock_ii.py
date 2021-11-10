"""
LeetCode :: November 2021 Challenge :: 122. Best Time to Buy and Sell Stock II
jramaswami
"""


import functools


class Solution:

    def maxProfit(self, prices):

        @functools.cache
        def buy(i):
            """Buy on day i"""
            # Base case:
            if i >= len(prices):
                return 0
            # You can choose to buy on day i.
            max_profit_buying = sell(i) - prices[i]
            # You can choose to skip day i.
            max_profit_not_buying = buy(i+1)
            return max(max_profit_buying, max_profit_not_buying)

        @functools.cache
        def sell(i):
            """Sell on day i."""
            # Base case:
            if i >= len(prices):
                return 0
            # You can choose to sell on day i.
            max_profit_selling = prices[i] + buy(i+1)
            # You can choose to hold on day i.
            max_profit_not_selling = sell(i+1)
            return max(max_profit_selling, max_profit_not_selling)

        return buy(0)


def test_1():
    prices = [7,1,5,3,6,4]
    expected = 7
    assert Solution().maxProfit(prices) == expected


def test_2():
    prices = [1,2,3,4,5]
    expected = 4
    assert Solution().maxProfit(prices) == expected


def test_3():
    prices = [7,6,4,3,1]
    expected = 0
    assert Solution().maxProfit(prices) == expected