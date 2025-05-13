"""
LeetCode
3335. Total Characters in String After Transformations I
May 2025 Challenge
jramaswami
"""


import collections


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = pow(10, 9) + 7
        prev_freqs = collections.Counter(s)
        next_freqs = collections.Counter()
        for _ in range(t):
            for c, n in prev_freqs.items():
                if c == 'z':
                    next_freqs['a'] += n
                    next_freqs['a'] %= MOD
                    next_freqs['b'] += n
                    next_freqs['b'] %= MOD
                else:
                    d = chr(ord(c)+1)
                    next_freqs[d] += n
                    next_freqs[d] %= MOD
            prev_freqs, next_freqs = next_freqs, collections.Counter()

        soln = 0
        for n in prev_freqs.values():
            soln += n
            soln %= MOD
        return soln % MOD