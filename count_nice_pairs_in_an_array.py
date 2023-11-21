"""
LeetCode
1814. Count Nice Pairs in an Array
November 2023 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = pow(10, 9) + 7
        # nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
        # nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
        def rev(n):
            m = 0
            while n:
                m *= 10
                n, r = divmod(n, 10)
                m += r
            return m

        # Compute rev(nums[i]) for all numbers
        nums0 = [rev(n) for n in nums]
        # Keep track of nums[i] - rev(nums[i]) seen so far.
        seen = collections.defaultdict(int)
        soln = 0
        for n, m in zip(nums, nums0):
            # nums[j] - rev(nums[j])
            t = n - m
            # Add all those we have seen before to the solution.
            soln = soln + seen[t]
            soln %= MOD
            seen[t] += 1
        return soln