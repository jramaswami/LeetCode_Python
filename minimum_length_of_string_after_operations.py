"""
LeetCode
3223. Minimum Length of String After Operations
January 2025 Challenge
jramaswami
"""


import collections


class Solution:
    def minimumLength(self, s: str) -> int:
        freqs = collections.Counter(s)
        soln = 0
        for x in freqs.values():
            if x % 2:
                soln += 1
            else:
                soln += 2
        return soln
