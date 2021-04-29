"""
Leet Code :: April 2021 Challenge ::  Find First and Last Position of Element in Sorted Array
jramaswami
"""
from typing import *


def lower_bound(nums, target):
    """Return rightmost element less than target."""
    lb = -1
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (high + low) // 2
        if nums[mid] < target:
            lb = max(lb, mid)
            low = mid + 1
        else:
            high = mid - 1
    return lb


def upper_bound(nums, target):
    """Return the leftmost element greater than target."""
    ub = len(nums)
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (high + low) // 2
        if nums[mid] > target:
            ub = min(ub, mid)
            high = mid - 1
        else:
            low = mid + 1

    return ub


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = lower_bound(nums, target)
        ub = upper_bound(nums, target)
        print(f"{lb=} {ub=}")
        if lb + 1 == ub:
            return [-1, -1]
        return [lb+1, ub-1]


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