"""
LeetCode :: September 2022 Challenge :: 1680. Concatenation of Consecutive Binary Numbers
jramaswami
"""


import math


class Solution:

    def concatenatedBinary(self, n: int) -> int:
        pows2 = [(i+1, pow(2, i)) for i in range(18)]
        MOD = pow(10, 9) + 7
        soln = 0
        shift = 0
        for x in range(n, 0, -1):
            while x < pows2[-1][1]:
                pows2.pop()
            p = pow(2, shift, MOD)
            t = (x * p) % MOD
            soln = (soln + t) % MOD
            shift += pows2[-1][0]
        return soln % MOD


def test_1():
    n = 1
    expected = 1
    assert Solution().concatenatedBinary(n) == expected


def test_2():
    n = 3
    expected = 27
    assert Solution().concatenatedBinary(n) == expected


def test_3():
    n = 12
    expected = 505379714
    assert Solution().concatenatedBinary(n) == expected


def test_4():
    "TLE on 354/403 testcase."
    n = 95830
    expected = 664636239
    assert Solution().concatenatedBinary(n) == expected