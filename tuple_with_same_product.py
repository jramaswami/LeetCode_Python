"""
LeetCode
1726. Tuple with Same Product
February 2025 Challenge
jramaswami
"""


import collections
import itertools


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        freqs = collections.Counter()
        for a, b in itertools.combinations(nums, 2):
            freqs[a*b] += 1
        soln = 0
        for n in freqs.values():
            soln += ((2 * n) * (2 * (n - 1)))
        return soln
