"""
LeetCode :: October Challenge :: 309. Best Time to Buy and Sell Stock with Cooldown
jramaswami

Thank You, Larry!
"""


import functools


class Solution:

    def maxProfit(self, prices):

        @functools.lru_cache(maxsize=None)
        def buy(i):
            """
            On day i, I can buy the stock because: (1) cooldown is over and (2)
            I do not currently own a stock. Return the maximum profit.
            """

            # Base case
            if i >= len(prices):
                return 0

            # I can choose *not* to buy the stock.  Given this I can still
            # buy a stock on the next day.
            max_profit_not_buying = buy(i+1)

            # I can choose to buy the stock.  This means that I will have to
            # sell the stock tomorrow or later.  Remember to deduct the cost
            # of buying the stock.
            max_profit_buying = sell(i+1) - prices[i]

            return max(max_profit_not_buying, max_profit_buying)

        @functools.lru_cache(maxsize=None)
        def sell(i):
            """
            On day i, I can sell a stock because I own one (the price of which
            has already been deducted from my profit).
            """

            # Base case
            if i >= len(prices):
                return 0

            # I can choose to hold the stock.  I will have to sell it tomorrow
            # or later.
            max_profit_not_selling = sell(i+1)

            # I can choose to sell the stock today.  This means I will get
            # todays price back and I can buy day after tomorrow.
            max_profit_selling = prices[i] + buy(i+2)

            return max(max_profit_not_selling, max_profit_selling)


        # On day 0, I can buy a stock because I do not own one and am not
        # in a cooling down period.
        return buy(0)



def test_1():
    prices = [1,2,3,0,2]
    expected = 3
    assert Solution().maxProfit(prices) == expected


def test_2():
    prices = [1]
    expected = 0
    assert Solution().maxProfit(prices) == expected
