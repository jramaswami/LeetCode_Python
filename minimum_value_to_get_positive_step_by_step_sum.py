"""
LeetCode :: November 2021 Challenge :: 1413. Minimum Value to Get Positive Step by Step Sum
jramaswami
"""


import itertools


class Solution:
    def minStartValue(self, nums):
        return 1 + max(0, -1 * min(itertools.accumulate(nums)))


def test_1():
    nums = [-3,2,-3,4,2]
    expected = 5
    assert Solution().minStartValue(nums) == expected


def test_2():
    nums = [1,2]
    expected = 1
    assert Solution().minStartValue(nums) == expected


def test_3():
    nums = [1,-2,-3]
    expected = 5
    assert Solution().minStartValue(nums) == expected