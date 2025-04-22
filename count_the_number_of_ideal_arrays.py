"""
LeetCode
2338. Count the Number of Ideal Arrays
April 2025 Challenge
jramawami
"""


import functools
import math


class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = pow(10, 9) + 7

        @functools.cache
        def get_comb(N, k):
            return math.comb(N, k) % MOD

        total = 0
        def gen():
            p = arr[-1]
            nonlocal total
            total += get_comb(n-1, len(arr) - 1)
            current = p + p
            while current <= maxValue:
                arr.append(current)
                gen()
                arr.pop()
                current += p

        arr = []
        for i in range(1, maxValue+1):
            arr.append(i)
            gen()
            arr.pop()
        return total % MOD




def test_1():
    n = 2
    maxValue = 5
    expected = 10
    assert Solution().idealArrays(n, maxValue) == expected


def test_2():
    n = 5
    maxValue = 3
    expected = 11
    assert Solution().idealArrays(n, maxValue) == expected
