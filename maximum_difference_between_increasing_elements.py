"""
LeetCode
2016. Maximum Difference Between Increasing Elements
June 2025 Challenge
jramaswami
"""


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        INF = pow(10,10)
        min_values = [INF for _ in nums]
        min_values[0] = nums[0]
        for i, n in enumerate(nums[1:], start=1):
            min_values[i] = min(n, min_values[i-1])

        soln = -1
        for i, n in enumerate(nums):
            if n > min_values[i]:
                soln = max(soln, n - min_values[i])
        return soln