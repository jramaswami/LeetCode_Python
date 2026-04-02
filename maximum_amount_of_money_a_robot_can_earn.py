"""
LeetCode
3418. Maximum Amount of Money Robot Can Earn
April 2026 Challenge
jramaswami
"""


from typing import List
import functools


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        INF = pow(10, 10)

        def neighbors(r, c):
            if r + 1 < len(coins):
                yield (r+1, c)
            if c + 1 < len(coins[r]):
                yield (r, c+1)

        @functools.cache
        def rec(r, c, neutralize):
            # Base case: bottom right
            if r == len(coins) - 1 and c == len(coins[r]) - 1:
                # Is this a robber
                if coins[r][c] < 0 and neutralize > 0:
                    return 0
                return coins[r][c]
            # Recursive case
            result = -INF
            if coins[r][c] < 0 and neutralize > 0:
                for r0, c0 in neighbors(r, c):
                    result = max(result, rec(r0, c0, neutralize - 1))
            for r0, c0 in neighbors(r, c):
                result = max(result, coins[r][c] + rec(r0, c0, neutralize))
            return result

        return rec(0, 0, 2)