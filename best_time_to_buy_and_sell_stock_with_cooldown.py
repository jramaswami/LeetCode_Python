"""
LeetCode :: October Challenge :: 309. Best Time to Buy and Sell Stock with Cooldown
jramaswami
"""

import collections
import enum


QItem = collections.namedtuple('QItem', ['state', 'profit', 'stock'])


class State(enum.Enum):
    CAN_BUY = enum.auto()
    CAN_SELL = enum.auto()
    COOLDOWN = enum.auto()


class Solution:

    def maxProfit(self, prices):
        queue = [QItem(State.CAN_BUY, 0, 0)]
        new_queue = []

        soln = 0
        for p in prices:
            for item in queue:
                soln = max(item.profit, soln)
                if item.state == State.CAN_BUY:
                    # Buy.
                    new_queue.append(QItem(State.CAN_SELL, item.profit, p))
                    # Don't buy.
                    new_queue.append(item)
                elif item.state == State.CAN_SELL:
                    # Sell
                    new_queue.append(QItem(State.COOLDOWN, item.profit + item.stock - p, 0))
                    # Don't sell.
                    new_queue.append(item)
                elif item.state == State.COOLDOWN:
                    # Cooldown period is over.
                    new_queue.append(QItem(State.CAN_BUY, item.profit, 0))
            queue, new_queue = new_queue, []

        return soln


def test_1():
    prices = [1,2,3,0,2]
    expected = 3
    assert Solution().maxProfit(prices) == expected


def test_2():
    prices = [1]
    expected = 0
    assert Solution().maxProfit(prices) == expected
