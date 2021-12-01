"""
LeetCode :: December 2021 Challenge :: 198. House Robber
jramaswami
"""


import functools


class Solution:

    def rob(self, nums):

        @functools.cache
        def can_rob(i):
            # Base case:
            if i >= len(nums):
                return 0

            # You can rob this house, but you will have to skip the next
            # in order to avoid alerting the police.
            max_rob = nums[i] + can_rob(i + 2)

            # You can skip this house and rob the next one.
            max_skip = can_rob(i + 1)

            return max(max_rob, max_skip)

        return can_rob(0)


def test_1():
    nums = [1,2,3,1]
    expected = 4
    assert Solution().rob(nums) == expected


def test_2():
    nums = [2,7,9,3,1]
    expected = 12
    assert Solution().rob(nums) == expected
