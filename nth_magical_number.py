"""
LeetCode :: December 2021 Challenge :: 878. Nth Magical Number
jramaswami
"""


import math


class Solution:

    def nthMagicalNumber(self, n, a, b):
        if a > b:
            a, b = b, a

        lo = 0
        hi = a * n
        l = (a * b) // math.gcd(a, b)
        soln = hi
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)

            ps = mid // a
            qs = mid // b
            rs = mid // l
            ts = ps + qs - rs
            if ts > n:
                hi = mid - 1
            elif ts < n:
                lo = mid + 1
            else:
                if mid % a == 0 or mid % b == 0:
                    soln = min(soln, mid)
                hi = mid - 1

        MOD = pow(10, 9) + 7
        return soln % MOD



def test_1():
    n = 1
    a = 2
    b = 3
    expected = 2
    assert Solution().nthMagicalNumber(n, a, b) == expected


def test_2():
    n = 4
    a = 2
    b = 3
    expected = 6
    assert Solution().nthMagicalNumber(n, a, b) == expected


def test_3():
    n = 5
    a = 2
    b = 4
    expected = 10
    assert Solution().nthMagicalNumber(n, a, b) == expected


def test_4():
    n = 3
    a = 6
    b = 4
    expected = 8
    assert Solution().nthMagicalNumber(n, a, b) == expected
