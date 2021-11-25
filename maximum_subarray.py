"""
LeetCode :: November 2021 Challenge :: 53. Maximum Subarray
jramaswami
"""


import math


class Solution:

    def maxSubArray(self, nums):
        # Kadane's algorithm
        curr_sum = 0
        # The soln must have at least one item in it.
        max_sum = -math.inf
        for n in nums:
            curr_sum = curr_sum + n
            max_sum = max(max_sum, curr_sum)
            curr_sum = max(curr_sum, 0)
        return max_sum


def test_1():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    expected = 6
    assert Solution().maxSubArray(nums) == expected


def test_2():
    nums = [1]
    expected = 1
    assert Solution().maxSubArray(nums) == expected


def test_3():
    nums = [-1]
    expected = -1
    assert Solution().maxSubArray(nums) == expected
