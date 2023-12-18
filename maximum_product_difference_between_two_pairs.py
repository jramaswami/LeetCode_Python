"""
LeetCode
1913. Maximum Product Difference Between Two Pairs
December 2023 Challenge
jramawami
"""



class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])