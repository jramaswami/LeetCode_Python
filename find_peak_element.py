"""
LeetCode :: July 2021 Challenge :: Find Peak Element
jramaswami
"""


from math import inf


class Solution:
    def findPeakElement(self, nums):
        lo = 0
        hi = len(nums) - 1
        while hi - lo > 1:
            mid = lo + ((hi - lo) // 2)
            if nums[mid] > nums[mid+1]:
                # the peak is the [lo .. mid]
                hi = mid
            else:
                # the peak is [mid .. hi]
                lo = mid

        # The peak is either lo or hi.
        if nums[lo] < nums[hi]:
            return hi
        else:
            return lo


def test_1():
    nums = [1,2,3,1]
    i = Solution().findPeakElement(nums)
    left = nums[i-1] if i - 1 >= 0 else -inf
    right = nums[i+1] if i + 1 < len(nums) else -inf
    assert nums[i] > left and nums[i] > right


def test_2():
    nums = [1,2,1,3,5,6,4]
    i = Solution().findPeakElement(nums)
    left = nums[i-1] if i - 1 >= 0 else -inf
    right = nums[i+1] if i + 1 < len(nums) else -inf
    assert nums[i] > left and nums[i] > right


def test_3():
    """WA"""
    nums = [1]
    i = Solution().findPeakElement(nums)
    left = nums[i-1] if i - 1 >= 0 else -inf
    right = nums[i+1] if i + 1 < len(nums) else -inf
    assert nums[i] > left and nums[i] > right
