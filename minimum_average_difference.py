"""
LeetCode
2256. Minimum Average Difference
December 2022 Challenge
jramaswami
"""


import math
from typing import *


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        left = 0
        total = sum(nums)
        N = len(nums)
        soln = (math.inf, math.inf)
        for i, n in enumerate(nums):
            left += n
            if N - i - 1:
                left_avg = left // (i+1)
                right_avg = (total - left) // (N - i - 1)
                avg_diff = abs(left_avg - right_avg)
            else:
                avg_diff = left // (i+1)
            soln = min((avg_diff, i), soln)
        return soln[1]


def test_1():
    nums = [2,5,3,9,5,3]
    expected = 3
    assert Solution().minimumAverageDifference(nums) == expected


def test_2():
    nums = [0]
    expected = 0
    assert Solution().minimumAverageDifference(nums) == expected
