"""
LeetCode
1780. Check if Number is a Sum of Powers of Three
March 2025 Challenge
jramaswami
"""


import functools


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        @functools.cache
        def rec(p, x):
            if x == 0:
                return True
            if x < 0:
                return False
            if p < 0:
                return False
            y = pow(3, p)
            return (
                rec(p-1, x - y) or
                rec(p-1, x)
            )
        
        return rec(16, n)
