"""
LeetCode
494. Target Sum
December 2024 Challenge
jramaswami
"""


import itertools
import operator
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        soln = 0
        for operators in itertools.product([operator.add, operator.sub], repeat=len(nums)):
            a = 0
            for b, op in zip(nums, operators):
                a = op(a, b)
            if a == target:
                soln += 1
        return soln


def test_1():
    nums = [1,1,1,1,1]
    target = 3
    expected = 5
    assert Solution().findTargetSumWays(nums, target) == expected



def test_2():
    nums = [1]
    target = 1
    expected = 1
    assert Solution().findTargetSumWays(nums, target) == expected


def test_3():
    "TLE"
    nums = [20,48,33,16,19,44,14,31,42,34,38,32,27,7,22,22,48,18,48,39]
    target = 1
    expected = 0
    assert Solution().findTargetSumWays(nums, target) == expected
