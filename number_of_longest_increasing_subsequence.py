"""
LeetCode
673. Number of Longest Increasing Subsequence
July 2023 Challenge
jramaswami
"""


from typing import *


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        dp_length = [1 for _ in nums]
        dp_count = [1 for _ in nums]

        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i+1:], start=i+1):
                if a < b:
                    if dp_length[i] + 1 > dp_length[j]:
                        dp_length[j] = dp_length[i] + 1
                        dp_count[j] = dp_count[i]
                    elif dp_length[i] + 1 == dp_length[j]:
                        dp_count[j] += dp_count[i]

        lis_length = max(dp_length)
        soln = sum(c for c, l in zip(dp_count, dp_length) if l == lis_length)
        return soln


def test_1():
    nums = [1,3,5,4,7]
    expected = 2
    assert Solution().findNumberOfLIS(nums) == expected


def test_2():
    nums = [2,2,2,2,2]
    expected = 5
    assert Solution().findNumberOfLIS(nums) == expected