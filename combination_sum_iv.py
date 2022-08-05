"""
LeetCode :: August 2022 Challenge :: Combination Sum IV
jramaswami
"""


from typing import *


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[sum][count of numbers] = count of ways
        dp = [[0 for _ in range(target+1)] for _ in range(target+1)]
        dp[0][0] = 1  # You can make the sum 0 one way.
        for count in range(target):
            for summ in range(target+1):
                for n in nums:
                    if dp[summ][count] > 0 and summ + n <= target:
                        dp[summ+n][count+1] += dp[summ][count]
        return sum(dp[-1])



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
