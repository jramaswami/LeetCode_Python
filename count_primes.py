"""
Leet Code :: May 2021 Challenge :: Count Primes
jramaswami
"""
from typing import *
from bisect import bisect_left


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        is_prime = [True for _ in range(n + 1)]
        is_prime[0] = is_prime[1] = 0

        soln = 1
        for k in range(4, n + 1, 2):
            is_prime[k] = False

        for j in range(3, n + 1, 2):
            if is_prime[j] and j < n:
                soln += 1
                for k in range(2 * j, n + 1, j):
                    is_prime[k] =  False
        return soln


def test_1():
    assert Solution().countPrimes(10) == 4


def test_2():
    assert Solution().countPrimes(0) == 0


def test_3():
    assert Solution().countPrimes(1) == 0


def test_4():
    assert Solution().countPrimes(2) == 0


def test_5():
    """WA"""
    assert Solution().countPrimes(999983) == 78497