"""
LeetCode
35. Search Insert Position
February 2023 Challenge
jramaswami
"""


class Solution:
    def searchInsert(self, nums, target):
        # Find the index of the rightmost item >= target.
        lo = 0
        hi = len(nums) - 1
        i = len(nums)
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if nums[mid] >= target:
                i = min(i, mid)
                hi = mid - 1
            else:
                lo = mid + 1
        return i


def test_1():
    nums = [1,3,5,6]
    target = 5
    expected = 2
    assert Solution().searchInsert(nums, target) == expected


def test_2():
    nums = [1,3,5,6]
    target = 2
    expected = 1
    assert Solution().searchInsert(nums, target) == expected


def test_3():
    nums = [1,3,5,6]
    target = 8
    expected = len(nums)
    assert Solution().searchInsert(nums, target) == expected


def test_4():
    nums = [1,3,5,6]
    target = -1
    expected = 0
    assert Solution().searchInsert(nums, target) == expected

