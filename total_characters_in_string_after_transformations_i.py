"""
LeetCode
3335. Total Characters in String After Transformations I
May 2025 Challenge
jramaswami
"""


import functools


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = pow(10, 9) + 7

        @functools.cache
        def rec(i, c):
            if i == 0:
                return 1
            if c == 'z':
                return (rec(i-1, 'a') + rec(i-1, 'b')) % MOD
            return rec(i-1, chr(ord(c)+1))

        soln = 0
        for c in s:
            soln += rec(t, c)
            soln %= MOD
        return soln % MOD