"""
LeetCode :: March 2021 Challenge :: Missing Number
jramaswami
"""
from typing import *


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # The sum of nums [1 .. N] should be N(N+1) // 2.
        # expected sum = actual sum + missing number
        # expected sum - actual sum = missing number
        N = len(nums)
        print((N * (N + 1)) // 2, sum(nums))
        return ((N * (N + 1)) // 2) - sum(nums)


def test_1():
    assert Solution().missingNumber([3,0,1]) == 2

def test_2():
    assert Solution().missingNumber([0,1]) == 2

def test_3():
    assert Solution().missingNumber([9,6,4,2,3,5,7,0,1]) == 8

def test_4():
    assert Solution().missingNumber([0]) == 1
