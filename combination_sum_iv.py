"""
LeetCode :: April Challenge 2021 :: Combination Sum IV
jramaswami
"""
from typing import *


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target+1)]
        for n in nums:
            if n <= target:
                dp[n] = 1

        nums0 = sorted(nums)
        for i, _ in enumerate(dp):
            if i:
                for n in nums0:
                    if i + n > target:
                        break
                    dp[i+n] += dp[i]
        return dp[target]


def test_1():
    nums = [1, 2, 3]
    target = 4
    expected = 7
    assert Solution().combinationSum4(nums, target) == expected


def test_2():
    nums = [9]
    target = 3
    expected = 0
    assert Solution().combinationSum4(nums, target) == expected


def test_3():
    nums = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    target = 10
    expected = 9
    assert Solution().combinationSum4(nums, target) == expected


def test_4():
    nums = [3,1,2,4]
    target = 4
    expected = 8
    assert Solution().combinationSum4(nums, target) == expected
