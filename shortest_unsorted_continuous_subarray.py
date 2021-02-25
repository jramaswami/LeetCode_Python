"""
LeetCode :: Shortest Unsorted Continuous Subarray
jramaswami
"""
from typing import *
from math import inf


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums0 = sorted(nums)
        left = inf
        right = -inf
        for i, (a, b) in enumerate(zip(nums, nums0)):
            if a != b:
                left = min(left, i)
                right = max(right, i)
        
        if left == inf:
            return 0
        return right - left + 1


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
