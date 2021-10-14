"""
LeetCode :: October 2021 Challenge :: 279. Perfect Squares
jramaswami
"""


from math import inf
from functools import lru_cache


import sys
sys.setrecursionlimit(pow(10, 9))


class Solution:
    def numSquares(self, n):

        @lru_cache(maxsize=None)
        def solve(k):
            """Return the minimum square sums to k."""
            if k == 0:
                return 0

            result = inf
            for j in range(1, k):
                sq = j * j
                delta = k - sq
                if delta >= 0:
                    result = min(result, 1 + solve(delta))

            return result

        return solve(n)



def test_1():
    assert Solution().numSquares(12) == 3


def test_2():
    assert Solution().numSquares(13) == 2


def test_3():
    """TLE"""
    assert Solution().numSquares(351) == 4


def test_4():
    """TLE"""
    assert Solution().numSquares(4586) == 2
