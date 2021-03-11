"""
LeetCode :: March 2021 Challenge :: Coin Change
jramaswami
"""
from typing import *
from math import inf

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf for _ in range(amount + 1)]
        dp[0] = 0
        for i, _ in enumerate(dp):
            for coin in coins:
                if i + coin <= amount:
                    dp[i + coin] = min(dp[i + coin], dp[i] + 1)
        return (-1 if dp[amount] == inf else dp[amount])
        

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
