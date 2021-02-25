"""
LeetCode :: Shortest Unsorted Continuous Subarray
jramaswami
"""
from typing import *
from math import inf


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left = None
        right = -inf
        curr_max = nums[0]
        curr_max_index = 0
        for i, n in enumerate(nums[1:], start = 1):
            # Find the first inversion.  
            if left is None and nums[i-1] > nums[i]:
                # This is the first inversion that has been seen.  This means
                # that the curr max should be the maximum number to the left of
                # the inversion.  Where is the first place that we saw this
                # current max? We have to go all the way back to that spot.
                left = curr_max_index

            # Keep track of the current max to the left and the first index
            # where it occurs.
            if n > curr_max:
                curr_max = n
                curr_max_index = i

            # Keep track of the right most item that is less than an element to
            # its left.
            if n < curr_max:
                right = max(right, i)

        # If left is still None, then there was no inversion.
        if left is None:
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

def test_6():
    nums = [2,1]
    assert Solution().findUnsortedSubarray(nums) == 2

def test_7():
    nums = [2,3,3,2,4]
    assert Solution().findUnsortedSubarray(nums) == 3

def test_8():
    nums = [1,2,4,5,3]
    assert Solution().findUnsortedSubarray(nums) == 3
