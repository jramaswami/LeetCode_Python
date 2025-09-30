"""
LeetCode
2221. Find Triangular Sum of an Array
September 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        prev = list(nums)
        curr = [0 for _ in nums]
        N = len(nums)
        for k in range(N-1):
            # Reduce length of curr
            while len(curr) > len(prev)-1:
                curr.pop()
            # Simulate
            for i, _ in enumerate(curr):
                curr[i] = (prev[i] + prev[i+1]) % 10
            curr, prev = prev, curr
        return prev[-1]