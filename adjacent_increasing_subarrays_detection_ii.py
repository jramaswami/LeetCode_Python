"""
LeetCode
3350. Adjacent Increasing Subarrays Detection II
October 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        soln = 0
        suffix = [0 for _ in nums]
        suffix[-1] = 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                suffix[i] = suffix[i+1] + 1
            else:
                suffix[i] = 1

        curr = 0
        for i in range(len(nums)-1):
            if i == 0 or nums[i-1] < nums[i]:
                curr += 1
            else:
                curr = 1
            soln = max(soln, min(curr, suffix[i+1]))

        return soln