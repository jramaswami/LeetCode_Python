"""
Leet Code :: Jump Game II
jramaswami
"""
from typing import *
from math import inf


class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [inf for _ in nums]
        dp[0] = 0
        for i, jmp in enumerate(nums):
            if dp[i] != inf:
                for j in range(1, jmp + 1):
                    if i + j < len(dp):
                        dp[i+j] = min(dp[i+j], dp[i]+1)
        return dp[-1]


def test_1():
    nums = [2,3,1,1,4]
    assert Solution().jump(nums) == 2


def test_2():
    nums = [2,3,0,1,4]
    assert Solution().jump(nums) == 2