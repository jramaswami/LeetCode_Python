"""
LeetCode
198. House Robber
December 2022 Challenge
jramaswami
"""


import functools


class Solution:

    def rob(self, nums):

        @functools.cache
        def rec(i):
            if i >= len(nums):
                return 0

            return max(
                # Rob this house.
                nums[i] + rec(i+2),
                # Don't rob this house.
                rec(i+1)
            )

        return rec(0)

def test_1():
    nums = [1,2,3,1]
    expected = 4
    assert Solution().rob(nums) == expected


def test_2():
    nums = [2,7,9,3,1]
    expected = 12
    assert Solution().rob(nums) == expected
