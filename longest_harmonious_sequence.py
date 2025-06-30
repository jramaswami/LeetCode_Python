"""
LeetCode
594. Longest Harmonious Subsequence
June 2025 Challenge
jramaswami
"""


import collections


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freqs = collections.Counter(nums)
        ns = list(sorted(freqs))
        soln = 0
        for a, b in zip(ns[:-1], ns[1:]):
            if b - a == 1:
                soln = max(soln, freqs[a] + freqs[b])
        return soln