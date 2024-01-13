"""
LeetCode
1347. Minimum Number of Steps to Make Two Strings Anagram
January 2024 Challenge
jramaswami
"""


import collections
import string


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq_s = collections.Counter(s)
        freq_t = collections.Counter(t)
        delta = 0
        for c in string.ascii_lowercase:
            delta += abs(freq_s[c] - freq_t[c])
        return delta // 2