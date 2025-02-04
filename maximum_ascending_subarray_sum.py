"""
LeetCode
1800. Maximum Ascending Subarray Sum
February 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        soln = nums[0]
        curr_sum = nums[0]
        prev_value = nums[0]
        for curr_value in nums[1:]:
            if curr_value > prev_value:
                curr_sum += curr_value
            else:
                curr_sum = curr_value
            soln = max(soln, curr_sum)
            prev_value = curr_value
        return soln     
