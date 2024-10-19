"""
LeetCode
1545. Find Kth Bit in Nth Binary String
October 2024 Challenge
jramaswami
"""


import functools


class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        @functools.cache        
        def inv(x):
             x0 = ["0" if t == "1" else "1" for t in x]
             x1 = x0[::-1]
             return ''.join(x1)

        @functools.cache
        def rec(i):
            if i == 1:
                return "0"
            x = rec(i-1)
            return x + "1" + inv(x)

        x = rec(n)
        return x[k-1]
