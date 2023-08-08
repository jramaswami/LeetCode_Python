"""
LeetCode
33. Search in Rotated Sorted Array
August 2023 Challenge
jramaswami
"""


from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            print(f"{lo=} {nums[lo]=} {hi=} {nums[hi]=} {mid=} {nums[mid]=} {target=}")
            if nums[mid] == target:
                return mid
            elif target < nums[mid] and target < nums[lo]:
                # If target is less than both nums[mid] and nums[lo] then it is
                # to the right of mid.
                lo = mid + 1
            elif target > nums[mid] and target > nums[-1]:
                # If target is greater than both nums[mid] and nums[hi] then it
                # is to the left of mid.
                hi = mid - 1
            elif nums[lo] <= target < nums[mid]:
                # If the target is between nums[lo] and nums[mid] then target
                # is to the left of mid
                hi = mid - 1
            elif nums[mid] < target <= nums[hi]:
                # If the target is between nums[mid] and nums[hi] then the target
                # is to the right of mid.
                lo = mid + 1
            else:
                raise Exception("Surprise!")
        return -1


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

