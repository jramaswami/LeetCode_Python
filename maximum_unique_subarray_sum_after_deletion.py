"""
LeetCode
3487. Maximum Unique Subarray Sum After Deletion
July 2025 Challenge
jramaswami
"""

from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # Try to remove all negative numbers
        # If all negative remove all but largest negative
        # Sum unique values
        nums0 = set(nums)
        if all(n < 0 for n in nums0):
            return max(n for n in nums0)
        return sum(n for n in nums0 if n >= 0)