"""
LeetCode
3423. Maximum Difference Between Adjacent Elements in a Circular Array
June 2025 Challenge
jramaswami
"""


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        soln = abs(nums[0] - nums[-1])
        for a, b in zip(nums[:-1], nums[1:]):
            soln = max(abs(a-b), soln)
        return soln