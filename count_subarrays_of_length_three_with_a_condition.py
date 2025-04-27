"""
LeetCode
3392. Count Subarrays of Length Three With a Condition
April 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        soln = 0
        for i, _ in enumerate(nums):
            if i + 2 < len(nums):
                t = 2 * (nums[i] + nums[i+2])
                if nums[i+1] == t:
                    soln += 1
        return soln
