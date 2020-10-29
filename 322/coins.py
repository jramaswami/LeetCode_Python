"""
Leetcode :: 322. Coin Change
https://leetcode.com/problems/coin-change/
"""
from typing import *
from math import inf

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf for _ in range(amount + 1)]
        dp[0] = 0
        for a in range(amount + 1):
            for coin in coins:
                if a + coin <= amount:
                    dp[a + coin] = min(dp[a + coin], dp[a] + 1)
        print(dp)
        if dp[amount] == inf:
            return -1
        return dp[amount]
