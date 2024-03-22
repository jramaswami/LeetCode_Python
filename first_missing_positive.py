"""
LeetCode
41. First Missing Positive
jramaswami
"""


import math


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            nums[i] = n if n > 0 else math.inf
        for i, n in enumerate(nums):
            n = abs(n)
            if 0 <= n-1 < len(nums):
                if nums[n-1] > 0:
                    nums[n-1] *= -1
        for i, n in enumerate(nums):
            if n > 0:
                return i + 1
        return len(nums)+1