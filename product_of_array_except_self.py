"""
LeetCode :: November 2021 Challenge :: 238. Product of Array Except Self
jramaswami
"""


import math


class Solution:
    def productExceptSelf(self, nums):
        zeros = nums.count(0)
        if zeros >= 2:
            return [0 for _ in nums]
        elif zeros == 1:
            p = math.prod(n for n in nums if n != 0)
            return [p if n == 0 else 0 for n in nums]
        else:
            p = math.prod(nums)
            return [p // n for n in nums]


def test_1():
    nums = [1,2,3,4]
    expected = [24,12,8,6]
    assert Solution().productExceptSelf(nums) == expected


def test_2():
    nums = [-1,1,0,-3,3]
    expected = [0,0,9,0,0]
    assert Solution().productExceptSelf(nums) == expected
