"""
LeetCode :: May 2022 Challenge :: Coin Change
jramaswami
"""


import math
import functools


class Solution:
    def coinChange(self, coins, amount):

        @functools.cache
        def solve(acc):
            if acc == 0:
                return 0

            result = math.inf
            for coin in coins:
                if acc - coin >= 0:
                    result = min(result, 1 + solve(acc - coin))
            return result


        soln = solve(amount)
        return (soln if soln < math.inf else -1)


def test_1():
    assert Solution().coinChange([1,2,5], 11) == 3

def test_2():
    assert Solution().coinChange([2], 3) == -1

def test_3():
    assert Solution().coinChange([1], 0) == 0

def test_4():
    assert Solution().coinChange([1], 1) == 1

def test_5():
    assert Solution().coinChange([1], 2) == 2
