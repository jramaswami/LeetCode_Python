"""
LeetCode
2163. Minimum Difference in Sums After Removal of Elements
July 2025 Challenge
jramaswami
"""


import heapq
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        soln = pow(10, 10)
        n = len(nums) // 3
        for i, _ in enumerate(nums):
            left = heapq.nsmallest(n, nums[:i])
            right = heapq.nlargest(n, nums[i:])
            if len(left) >= n and len(right) >= n:
                soln = min(soln, sum(left) - sum(right))
        return soln