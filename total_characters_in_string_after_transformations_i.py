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
        # Convert array to integers
        prev_freqs = [0 for _ in range(26)]
        ord_a = ord('a')
        for c in s:
            x = ord(c) - ord_a
            prev_freqs[x] += 1
        next_freqs = [0 for _ in range(26)]
        for _ in range(t):
            for c, n in enumerate(prev_freqs):
                if c == 25:
                    next_freqs[0] += n
                    next_freqs[0] %= MOD
                    next_freqs[1] += n
                    next_freqs[1] %= MOD
                else:
                    next_freqs[c+1] += n
                    next_freqs[c+1] %= MOD
            prev_freqs, next_freqs = next_freqs, [0 for _ in range(26)]

        soln = 0
        for n in prev_freqs:
            soln += n
            soln %= MOD
        return soln % MOD