"""
LeetCode :: Shortest Unsorted Continuous Subarray
jramaswami
"""
from typing import *
from math import inf


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left_i = inf
        curr_min = nums[-1]
        for negi, n in enumerate(reversed(nums), start=-(len(nums)-1)):
            curr_min = min(n, curr_min)
            if n > curr_min:
                left_i = min(-negi, left_i)

        right_i = -inf
        curr_max = nums[0]
        for i, n in enumerate(nums):
            curr_max = max(n, curr_max)
            if n < curr_max:
                right_i = max(i, right_i)
        
        if left_i == inf:
            return 0
        return right_i - left_i + 1
        

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
