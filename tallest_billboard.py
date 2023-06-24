"""
LeetCode
956. Tallest Billboard
June 2023 Challenge
jramaswami

Thank You Larry!
"""


import functools
import math
from typing import List


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        @functools.cache
        def rec(index, delta):
            if index >= len(rods):
                if delta == 0:
                    return 0
                return -math.inf
            if delta < 0:
                return rec(index, -delta)
            return max(
                rec(index + 1, delta + rods[index]) + rods[index],
                rec(index + 1, delta - rods[index]),
                rec(index + 1, delta)
            )
        return rec(0, 0)
                    

def test_1():
    rods = [1,2,3,6]
    expected = 6
    assert Solution().tallestBillboard(rods) == expected


def test_2():
    rods = [1,2,3,4,5,6]
    expected = 10
    assert Solution().tallestBillboard(rods) == expected


def test_3():
    rods = [1,2]
    expected = 0
    assert Solution().tallestBillboard(rods) == expected


def test_4():
    "TLE"
    rods = [1,2,4,8,16,32,64,128,256,512,50,50,50,150,150,150,100,100,100,123]
    expected = 1023
    assert Solution().tallestBillboard(rods) == expected


def test_5():
    "TLE"
    rods = [102,101,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]
    expected = 900
    assert Solution().tallestBillboard(rods) == expected


def test_6():
    "WA"
    rods = [3,4,3,3,2]
    expected = 6
    assert Solution().tallestBillboard(rods) == expected
