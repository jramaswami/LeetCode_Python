"""
LeetCode
3016. Minimum Number of Pushes to Type Word II
August 2024 Challenge
jramaswami
"""


import collections


class Solution:
    def minimumPushes(self, word: str) -> int:
        freqs = collections.Counter(word)
        freqs0 = [(v, k) for k, v in freqs.items()]
        freqs0.sort(reverse=True)
        soln = 0
        for i, (n, t) in enumerate(freqs0):
            x = 1 + (i // 8)
            soln += (x * n)
        return soln