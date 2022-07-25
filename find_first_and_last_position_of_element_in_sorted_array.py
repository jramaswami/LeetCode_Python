"""
Leet Code :: July 2022 Challenge ::  Find First and Last Position of Element in Sorted Array
jramaswami
"""


from typing import *


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        lo = 0
        hi = len(nums) - 1
        left = len(nums)
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if nums[mid] == target:
                left = min(left, mid)
                # Try to find one lower.
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        # We did not find target if i is len(nums).
        if left == len(nums):
            return [-1, -1]

        # Target was found, find the x such that x is > than target.
        lo = left
        hi = len(nums) - 1
        right = left
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if nums[mid] == target:
                right = max(right, mid)
                lo = mid + 1
            elif nums[mid] > target:
                # Try to the left.
                hi = mid - 1
        return [left, right]


def test_1():
    nums = [5,7,7,8,8,10]
    target = 8
    expected = [3,4]
    assert Solution().searchRange(nums, target) == expected


def test_2():
    nums = [5,7,7,8,8,10]
    target = 6
    expected = [-1,-1]
    assert Solution().searchRange(nums, target) == expected


def test_3():
    nums = []
    target = 0
    expected = [-1,-1]
    assert Solution().searchRange(nums, target) == expected


def test_4():
    nums = [1, 1, 1, 1, 1]
    target = 1
    expected = [0, 4]
    assert Solution().searchRange(nums, target) == expected


def test_5():
    nums = [0, 0, 1, 1, 1, 1, 1]
    target = 1
    expected = [2, 6]
    assert Solution().searchRange(nums, target) == expected


def test_6():
    nums = [1, 1, 1, 1, 1, 2, 2]
    target = 1
    expected = [0, 4]
    assert Solution().searchRange(nums, target) == expected
