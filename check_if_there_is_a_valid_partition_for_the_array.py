"""
LeetCode
2369. Check if There is a Valid Partition For The Array
August 2023 Challenge
jramaswami
"""


import functools
from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:

        @functools.cache
        def rec(i):
            if i >= len(nums):
                return True

            result = False
            if i+1 < len(nums) and nums[i] == nums[i+1]:
                result = (result or rec(i+2))
            if i+2 < len(nums) and nums[i] == nums[i+1] and nums[i+1] == nums[i+2]:
                result = (result or rec(i+3))
            if i+2 < len(nums) and nums[i] + 1 == nums[i+1] and nums[i+1] + 1 == nums[i+2]:
                result = (result or rec(i+3))
            return result

        return rec(0)


def test_1():
    nums = [4,4,4,5,6]
    expected = True
    assert Solution().validPartition(nums) == expected


def test_2():
    nums = [1,1,1,2]
    expected = False
    assert Solution().validPartition(nums) == expected


test_1()