"""
LeetCode
1464. Maximum Product of Two Elements in an Array
December 2023 Challenge
jramaswami
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-2] - 1) * (nums[-1] - 1)