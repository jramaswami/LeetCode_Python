"""
LeetCode
33. Search in Rotated Sorted Array
August 2023 Challenge
jramaswami
"""


from typing import *


def find_pivot(nums: List[int]) -> int:
    "Return the index of the pivot or len(nums) if there is no pivot."
    # Index of left most item less than nums[0]
    lo = 1
    hi = len(nums) - 1
    pivot = len(nums)
    while lo <= hi:
        mid = lo + ((hi - lo) // 2)
        if nums[mid] <= nums[0]:
            # Go left
            hi = mid - 1
            pivot = min(pivot, mid)
        else:
            # Go right
            lo = mid + 1
    return pivot


def binsearch(nums, target, lo, hi):
    while lo <= hi:
        mid = lo + ((hi - lo) // 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p = find_pivot(nums)
        if p == len(nums):
            # Just a regular binary search.
            return binsearch(nums, target, 0, len(nums)-1)
        if target < nums[0]:
            # Search the right half.
            return binsearch(nums, target, p, len(nums)-1)
        return binsearch(nums, target, 0, p-1)



import collections


def test_find_pivot_1():
    nums = [4,5,6,7,0,1,2]
    expected = 4
    assert find_pivot(nums) == expected


def test_find_pivot_2():
    nums = [1]
    expected = 1
    assert find_pivot(nums) == expected


def test_find_pivot_3():
    nums = [1,2,3,4,5,6,7,8,9]
    expected = len(nums)
    assert find_pivot(nums) == expected


def test_find_pivot_4():
    nums = [2,3,4,5,6,7,8,1]
    expected = len(nums) - 1
    assert find_pivot(nums) == expected


def test_find_pivot_5():
    nums = [9,1,2,3,4,5,6,7,8]
    expected = 1
    assert find_pivot(nums) == expected


def test_find_pivot_bf():
    nums = collections.deque(range(20))
    for r in range(20):
        nums.rotate(-r)
        nums0 = list(nums)
        _, expected = min(((t, i) for i, t in enumerate(nums0)))
        result = find_pivot(nums0)
        print(nums0, expected, result)
        assert result % len(nums) == expected


def test_1():
    nums = [4,5,6,7,0,1,2]
    target = 0
    expected = 4
    assert Solution().search(nums, target) == expected


def test_2():
    nums = [4,5,6,7,0,1,2]
    target = 3
    expected = -1
    assert Solution().search(nums, target) == expected


def test_3():
    nums = [1]
    target = 0
    expected = -1
    assert Solution().search(nums, target) == expected


def test_4():
    "RTE"
    nums = [1,3,5]
    target = 2
    expected = -1
    assert Solution().search(nums, target) == expected


def test_5():
    "WA"
    nums = [4,5,6,7,0,1,2]
    target = 6
    expected = 2
    assert Solution().search(nums, target) == expected


def test_6():
    "WA"
    nums = [4,5,6,7,8,1,2,3]
    target = 8
    expected = 4
    assert Solution().search(nums, target) == expected