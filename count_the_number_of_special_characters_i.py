"""
LeetCode
3120. Count the Number of Special Characters I
May 2026 Challenge
jramaswami
"""


import collections
import string


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        soln = 0
        freqs = collections.Counter(word)
        for lc, uc in zip(string.ascii_lowercase, string.ascii_uppercase):
            if freqs[lc] > 0 and freqs[uc] > 0:
                soln += 1
        return soln