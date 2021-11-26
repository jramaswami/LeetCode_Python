"""
LeetCode :: November 2021 Challenge :: 35. Search Insert Position
jramaswami
"""


class Solution:
    def searchInsert(self, nums, target):
        # Binary search for the lowest index such that nums[i] >= target.
        soln = len(nums)
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if nums[mid] >= target:
                soln = min(soln, mid)
                hi = mid - 1
            else:
                lo = mid + 1
        return soln


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

