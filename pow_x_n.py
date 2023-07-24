"""
LeetCode
50. Pow(x, n)
July 2023 Challenge
jramaswami
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:

        def binpow(t, exp):
            result = 1.0
            while exp:
                if exp & 1:
                    result = result * t
                t = t * t
                exp >>= 1
            return result

        y = binpow(x, abs(n))
        if n < 0:
            y = 1.0 / y
        return y


EPS = pow(10, -5)


def test_1():
    x = 2.0
    n = 10
    expected = 1024.0
    assert Solution().myPow(x, n) == expected


def test_2():
    x = 2.1
    n = 3
    expected = 9.2610
    assert abs(Solution().myPow(x, n) - expected) < EPS


def test_3():
    x = 2.0
    n = -2
    expected = 0.250
    assert abs(Solution().myPow(x, n) - expected) < EPS