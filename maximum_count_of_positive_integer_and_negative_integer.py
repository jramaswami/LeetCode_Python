"""
LeetCode
2529. Maximum Count of Positive Integer and Negative Integer
March 2025 Challenge
jramaswami
"""


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(sum(1 for n in nums if n < 0), sum(1 for n in nums if n > 0))
