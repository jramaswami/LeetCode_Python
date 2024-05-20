"""
LeetCode
1863. Sum of All Subset XOR Totals
May 2024 Challenge
jramaswami
"""


import functools
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        @functools.cache
        def rec(i, acc):
            if i >= len(nums):
                return 0

            # Without nums[i]
            result = rec(i+1, acc)
            # With nums[i]
            acc0 = acc ^ nums[i]
            result += acc0 + rec(i+1, acc0)
            return result

        return rec(0, 0)


def test_1():
    nums = [1, 3]
    expected = 6
    assert Solution().subsetXORSum(nums) == expected


def test_2():
    nums = [5, 1, 6]
    expected = 28
    assert Solution().subsetXORSum(nums) == expected


def test_3():
    nums = [3,4,5,6,7,8]
    expected = 480
    assert Solution().subsetXORSum(nums) == expected