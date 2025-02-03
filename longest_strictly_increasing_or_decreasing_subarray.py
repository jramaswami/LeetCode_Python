"""
LeetCode
3105. Longest Strictly Increasing or Strictly Decreasing Subarray
February 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        soln = 1
        # Strictly decreasing
        prev_value = nums[0]
        curr_length = 1
        for curr_value in nums[1:]:
            if curr_value < prev_value:
                curr_length += 1
            else:
                curr_length = 1
            soln = max(soln, curr_length)
            prev_value = curr_value
        # Strictly increasing
        prev_value = nums[0]
        curr_length = 1
        for curr_value in nums[1:]:
            if curr_value > prev_value:
                curr_length += 1
            else:
                curr_length = 1
            soln = max(soln, curr_length)
            prev_value = curr_value
        return soln    
