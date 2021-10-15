"""
LeetCode :: October Challenge :: 309. Best Time to Buy and Sell Stock with Cooldown
jramaswami
"""

import collections
import enum


QItem = collections.namedtuple('QItem', ['state', 'profit'])


class State(enum.IntEnum):
    CAN_BUY = 0
    CAN_SELL = 1
    COOLDOWN = 2


class Solution:

    def maxProfit(self, prices):
        prev = collections.defaultdict(int)
        prev[QItem(State.CAN_BUY, 0)] = 0
        curr = collections.defaultdict(int)

        soln = 0
        for price in prices:
            for item, holding in prev.items():
                soln = max(soln, item.profit)
                if item.state == State.CAN_BUY:
                    # Buy.
                    next_item = QItem(State.CAN_SELL, item.profit)
                    curr[next_item] = max(curr[next_item], price)
                    # Do not buy.
                    curr[item] = max(curr[item], holding)
                if item.state == State.CAN_SELL:
                    # Sell.
                    profit = holding - price
                    next_item = QItem(State.CAN_SELL, item.profit + profit)
                    curr[next_item] = max(curr[next_item], 0)
                    # Don't sell.
                    curr[item] = max(curr[item], holding)
                if item.state == State.COOLDOWN:
                    # Cooldown over.
                    curr[item] = max(QItem(State.CAN_BUY, item.profit), 0)
            prev, curr = curr, collections.defaultdict(int)

        return soln


def test_1():
    prices = [1,2,3,0,2]
    expected = 3
    assert Solution().maxProfit(prices) == expected


def test_2():
    prices = [1]
    expected = 0
    assert Solution().maxProfit(prices) == expected
