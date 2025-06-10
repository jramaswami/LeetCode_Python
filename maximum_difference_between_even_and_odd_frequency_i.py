"""
LeetCode
3442. Maximum Difference Between Even and Odd Frequency I
June 2025 Challenge
jramaswami
"""


import collections


class Solution:
    def maxDifference(self, s: str) -> int:
        freqs = collections.Counter(s)
        max_odd_freq = -pow(10, 10)
        min_even_freq = pow(10, 10)
        for x in freqs.values():
            if x % 2 == 1:
                max_odd_freq = max(max_odd_freq, x)
            else:
                min_even_freq = min(min_even_freq, x)

        return max_odd_freq - min_even_freq