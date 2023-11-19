"""
LeetCode
1887. Reduction Operations to Make the Array Elements Equal
November 2023 Challenge
jramaswami
"""


from typing import List
import collections


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        freqs = tuple(sorted(collections.Counter(nums).items(),reverse=True))
        soln = 0
        for i, (_, f) in enumerate(freqs[:-1]):
            soln += ((len(freqs) - i - 1) * f)
        return soln