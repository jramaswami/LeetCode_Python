"""
LeetCode :: Shortest Unsorted Continuous Subarray
jramaswami
"""
from typing import *
from math import inf


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left = inf
        right = -inf
        for i, n in enumerate(nums[1:], start = 1):
            # Find an inversion.  
            if nums[i-1] > nums[i]:
                # Keep track of the leftmost start of an inversion.
                left = min(left, i-1)
                # Keep track of the right most start of an inversion.
                right = max(right, i)
        # If left is still inf, then there was no inversion.
        if left == inf:
            return 0
        # Otherwise, you will have to sort A[left:right] inclusive (so add 1).
        return 1 + right - left


def test_1():
    nums = [2,6,4,8,10,9,15]
    assert Solution().findUnsortedSubarray(nums) == 5

def test_2():
    nums = [1,2,3,4]
    assert Solution().findUnsortedSubarray(nums) == 0

def test_3():
    nums = [1]
    assert Solution().findUnsortedSubarray(nums) == 0

def test_4():
    nums = [4,3,2,1]
    assert Solution().findUnsortedSubarray(nums) == 4

def test_5():
    nums = [1,3,2,2,2]
    assert Solution().findUnsortedSubarray(nums) == 4
