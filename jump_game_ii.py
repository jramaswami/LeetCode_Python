"""
Leet Code
Jump Game II
February 2023
jramaswami
"""


from typing import *
import math


class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [math.inf for _ in nums]
        dp[0] = 0
        for i, x in enumerate(nums):
            for j in range(i+1, min(i+x+1, len(nums))):
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1]


def test_1():
    nums = [2,3,1,1,4]
    assert Solution().jump(nums) == 2


def test_2():
    nums = [2,3,0,1,4]
    assert Solution().jump(nums) == 2


def test_3():
    nums = [2,3,1,1,4,2,3,1,1,4,2,3,1,1,4]
    assert Solution().jump(nums) == 6


def test_4():
    nums = [2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4]
    assert Solution().jump(nums) == 42


def test_5():
    nums = [0]
    assert Solution().jump(nums) == 0
