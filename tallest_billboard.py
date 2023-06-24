"""
LeetCode
956. Tallest Billboard
June 2023 Challenge
jramaswami
"""


import functools
from typing import List


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:

        @functools.cache
        def rec(i, left, right):
            # Base case:
            if i >= len(rods):
                # If the rods are equal, return the current height.
                if left == right:
                    return left
                # Unequal rods cannot be used, return 0.
                return 0

            # If we have equal heights, start with that as our max.
            # If they are unequal, then we cannot use them, start with 0.
            result = (left if left == right else 0)
            result = max(
                result,
                # Include this rod on the left
                rec(i+1, left+rods[i], right),
                # Include this rod on the right
                rec(i+1, left, right+rods[i]),
                # Skip this rod
                rec(i+1, left, right)
            )
            return result

        return rec(0, 0, 0)


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
