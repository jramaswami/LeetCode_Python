"""
LeetCode
2657. Find the Prefix Common Array of Two Arrays
January 2025 Challenge
jramaswami
"""


import collections


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        soln = []
        curr = 0
        freqs = collections.Counter()
        for a, b in zip(A, B):
            freqs[a] += 1
            if freqs[a] == 2:
                curr += 1
            freqs[b] += 1
            if freqs[b] == 2:
                curr += 1
            soln.append(curr)
        return soln
