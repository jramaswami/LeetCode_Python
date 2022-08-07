"""
LeetCode :: 724. Find Pivot Index
jramaswami
"""


from typing import *
import itertools


class Solution:

    def pivotIndex(self, nums: List[int]) -> int:
        prefix = list(itertools.accumulate(nums))

        def get_sum(left, right):
            "Return sum of nums[left:right+1]"
            if left > right:
                return 0
            if left - 1 < 0:
                return prefix[right]
            return prefix[right] - prefix[left-1]

        for p, _ in enumerate(nums):
            left_sum = get_sum(0, p-1)
            right_sum = get_sum(p+1, len(nums) - 1)
            if left_sum == right_sum:
                return p
        return -1



def test_1():
    nums = [1,7,3,6,5,6]
    expected = 3
    assert Solution().pivotIndex(nums) == expected


def test_2():
    nums = [1,2,3]
    expected = -1
    assert Solution().pivotIndex(nums) == expected


def test_3():
    nums = [2,1,-1]
    expected = 0
    assert Solution().pivotIndex(nums) == expected
