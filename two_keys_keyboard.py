"""
LeetCode
650. 2 Keys Keyboard
August 2024 Challenge
jramaswami
"""


import functools


class Solution:
    def minSteps(self, n: int) -> int:
        INF = pow(10, 10)

        @functools.cache
        def copy(chars, buffer):
            if chars > n:
                return INF
            if chars == n:
                return 0
            return 1+paste(chars, chars)
        
        @functools.cache
        def paste(chars, buffer):
            if chars > n:
                return INF
            if chars == n:
                return 0
            return min(
                1+copy(chars+buffer, buffer),
                1+paste(chars+buffer, buffer)
            )

        return copy(1, 0)
