"""
LeetCode
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
June 2024 Challenge
jramaswami
"""


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        INF = pow(10, 10)
        soln = 0
        for i, _ in enumerate(nums):
            curr_min = INF
            curr_max = -INF
            for j, n in enumerate(nums[i:], start=i):
                curr_min = min(curr_min, n)
                curr_max = max(curr_max, n)
                if curr_max - curr_min <= limit:
                    soln = max(soln, j - i + 1)
        return soln
