"""
LeetCode
2598. Smallest Missing Non-negative Integer After Operations
October 2025 Challenge
jramaswami

Thank You Larry!
"""


import collections
from typing import List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        freqs = collections.Counter(n % value for n in nums)
        soln = 0
        while freqs[soln % value] > 0:
            freqs[soln % value] -= 1
            soln += 1
        return soln