"""
LeetCode :: October 2021 Challenge :: 279. Perfect Squares
jramaswami
"""

import math


class Solution:
    def numSquares(self, n):
        # DP[sum] = minimum number of squares required
        perfect_sums = [math.inf for _ in range(n+1)]

        # Generate perfect squares
        k = 1
        perfect_squares = []
        while k * k <= n:
            perfect_squares.append(k * k)
            perfect_sums[k * k] = 1
            k += 1

        # Perform dp
        for i in range(1, n+1):
            if perfect_sums[i] < math.inf:
                for k in perfect_squares:
                    if k + i > n:
                        break
                    perfect_sums[i + k] = min(perfect_sums[i + k], perfect_sums[i] + 1)
        return perfect_sums[n]


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


def test_5():
    """TLE"""
    assert Solution().numSquares(1) == 1


def test_6():
    "TLE"
    n = 3258
    assert Solution().numSquares(n) == 2
