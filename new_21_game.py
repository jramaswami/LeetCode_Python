"""
LeetCode
837. New 21 Game
May 2023 Challenge
jramaswami
"""


import functools


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:

        @functools.cache
        def rec(currScore):
            # Base case: stop when you reach k points.
            if currScore >= k:
                return 1 if currScore <= n else 0
            return sum(rec(currScore + draw) for draw in range(1, maxPts+1)) / maxPts

        return rec(0)


EPS = pow(10, -5)


def test_1():
    n = 10
    k = 1
    maxPts = 10
    expected = 1.00000
    assert abs(Solution().new21Game(n, k, maxPts) - expected) < EPS


def test_2():
    n = 6
    k = 1
    maxPts = 10
    expected = 0.60000
    assert abs(Solution().new21Game(n, k, maxPts) - expected) < EPS


def test_3():
    n = 21
    k = 17
    maxPts = 10
    expected = 0.73278
    assert abs(Solution().new21Game(n, k, maxPts) - expected) < EPS
