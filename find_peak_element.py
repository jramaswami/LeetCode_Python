"""
LeetCode :: July 2021 Challenge :: Find Peak Element
jramaswami
"""


from math import inf


class Solution:
    def findPeakElement(self, nums):
        for i, mid in enumerate(nums):
            left = nums[i-1] if i - 1 >= 0 else -inf
            right = nums[i+1] if i + 1 < len(nums) else -inf
            if left < mid and mid > right:
                return i


def test_1():
    nums = [1,2,3,1]
    assert Solution().findPeakElement(nums) == 2


def test_2():
    nums = [1,2,1,3,5,6,4]
    assert Solution().findPeakElement(nums) == 1


def test_3():
    """WA"""
    nums = [1]
    assert Solution().findPeakElement(nums) == 0
