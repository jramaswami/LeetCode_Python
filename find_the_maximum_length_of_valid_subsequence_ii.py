"""
LeetCode
3202. Find the Maximum Length of Valid Subsequence II
July 2025 Challenge
jramaswami
"""


import functools
from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:

        @functools.cache
        def rec(i, prev, x):
            if i >= len(nums):
                return 0

            if (prev + nums[i]) % k == x:
                return 1 + rec(i+1, nums[i], x)
            return rec(i+1, prev, x)

        soln = 0
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i+1:], start=i+1):
                x = (a + b) % k
                soln = max(soln, 2 + rec(j+1, b, x))
        return soln