"""
LeetCode :: March 2021 Challenge :: Wiggle Subsequence
jramaswami
"""
from typing import *
from math import inf


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        increasing_dp = [1 for _ in nums]
        decreasing_dp = [1 for _ in nums]
        for i, n in enumerate(nums):
            for j, m in enumerate(nums[i+1:], start=i+1):
                # If n < m, then m can be increasing from n.
                if n < m:
                    increasing_dp[j] = max(increasing_dp[j], 1 + decreasing_dp[i])
                # If n > m then m can be decreasing from m.
                if n > m:
                    decreasing_dp[j] = max(decreasing_dp[j], 1 + increasing_dp[i])

        return max(max(decreasing_dp), max(increasing_dp))



def test_1():
    nums = [1,7,4,9,2,5]
    assert Solution().wiggleMaxLength(nums) == 6

def test_2():
    nums = [1,2,3,4,5,6,7,8,9]
    assert Solution().wiggleMaxLength(nums) == 2

def test_3():
    """TLE"""
    nums = [33,53,12,64,50,41,45,21,97,35,47,92,39,0,93,55,40,46,69,42,6,95,51,68,72,9,32,84,34,64,6,2,26,98,3,43,30,60,3,68,82,9,97,19,27,98,99,4,30,96,37,9,78,43,64,4,65,30,84,90,87,64,18,50,60,1,40,32,48,50,76,100,57,29,63,53,46,57,93,98,42,80,82,9,41,55,69,84,82,79,30,79,18,97,67,23,52,38,74,15]
    assert Solution().wiggleMaxLength(nums) == 67
