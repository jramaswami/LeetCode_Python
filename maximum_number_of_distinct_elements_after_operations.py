"""
LeetCode
3397. Maximum Number of Distinct Elements After Operations
October 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        prev = -pow(10, 10)
        soln = 0
        for n in nums:
            x = max(prev+1, n - k)
            if x <= n + k:
                soln += 1
                prev = x
        return soln