"""
LeetCode
409. Longest Palindrome
June 2024 Challenge
jramaswami
"""


import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        freqs = collections.Counter(s)
        soln = 0
        is_odd = 0
        for k, f in freqs.items():
            if f % 2 == 0:
                soln += f
            else:
                is_odd = 1
                soln += (f - 1)
        return soln + is_odd
