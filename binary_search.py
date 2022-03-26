"""
LeetCode :: March 2022 Challenge :: Binary Search
jramaswami
"""


class Solution:
    def search(self, nums, target):
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1


def test_1():
    nums = [-1,0,3,5,9,12]
    target = 9
    expected = 4
    assert Solution().search(nums, target) == expected


def test_2():
    nums = [-1,0,3,5,9,12]
    target = 2
    expected = -1
    assert Solution().search(nums, target) == expected
