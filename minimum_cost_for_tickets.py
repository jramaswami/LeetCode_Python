"""
LeetCode
983. Minimum Cost For Tickets
March 2023 Challenge
jramaswami
"""


import functools
import math
from typing import *


class Solution:
    def mincostTickets(self, riding_days: List[int], ticket_costs: List[int]) -> int:

        @functools.cache
        def rec(i, ticket_days, bought_on):
            if i >= len(riding_days):
                return 0

            result = math.inf
            if riding_days[i] - bought_on < ticket_days:
                # I can still ride today, don't buy a ticket.
                result = min(
                    result,
                    rec(i+1, ticket_days, bought_on)
                )

            # Buy new ticket today.
            for c, d in zip(ticket_costs,(1,7,30)):
                result = min(
                    result,
                    c + rec(i+1, d, riding_days[i])
                )
            return result

        return rec(0, 0, 0)


def test_1():
    days = [1,4,6,7,8,20]
    costs = [2,7,15]
    expected = 11
    assert Solution().mincostTickets(days, costs) == expected


def test_2():
    days = [1,2,3,4,5,6,7,8,9,10,30,31]
    costs = [2,7,15]
    expected = 17
    assert Solution().mincostTickets(days, costs) == expected