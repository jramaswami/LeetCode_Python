"""
LeetCode :: January 2022 Challenge :: 875. Koko Eating Bananas
jramaswami
"""


import math


class Solution:
    def minEatingSpeed(self, piles, h):

        def can_eat(k):
            t = 0
            for b in piles:
                t += math.ceil(b / k)
            return t <= h

        # Binary search for the answer.
        soln = max(piles)
        lo = 1
        hi = soln
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if can_eat(mid):
                hi = mid - 1
                soln = min(soln, mid)
            else:
                lo = mid + 1
        return soln


def test_1():
    piles = [3,6,7,11]
    h = 8
    expected = 4
    assert Solution().minEatingSpeed(piles, h) == expected


def test_2():
    piles = [30,11,23,4,20]
    h = 5
    expected = 30
    assert Solution().minEatingSpeed(piles, h) == expected


def test_3():
    piles = [30,11,23,4,20]
    h = 6
    expected = 23
    assert Solution().minEatingSpeed(piles, h) == expected


def test_4():
    "TLE"
    piles = [312884470]
    h = 312884469
    expected = 2
    assert Solution().minEatingSpeed(piles, h) == expected
