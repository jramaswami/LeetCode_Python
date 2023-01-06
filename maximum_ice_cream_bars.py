"""
LeetCode
1833. Maximum Ice Cream Bars
January 2023 Challenge
jramaswami
"""


from typing import *


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        soln = 0
        total = 0
        for c in costs:
            total += c
            if total > coins:
                break
            soln += 1
        return soln


def test_1():
    costs = [1,3,2,4,1]
    coins = 7
    expected = 4
    assert Solution().maxIceCream(costs, coins) == expected


def test_2():
    costs = [10,6,8,7,7,8]
    coins = 5
    expected = 0
    assert Solution().maxIceCream(costs, coins) == expected


def test_3():
    costs = [1,6,3,1,2,5]
    coins = 20
    expected = 6
    assert Solution().maxIceCream(costs, coins) == expected