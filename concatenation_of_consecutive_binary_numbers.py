"""
LeetCode :: September 2022 Challenge :: 1680. Concatenation of Consecutive Binary Numbers
jramaswami

Thank You Larry!
"""


class Solution:

    def concatenatedBinary(self, n: int) -> int:
        MOD = pow(10, 9) + 7
        soln = 0
        shift = 0
        for x in range(1, n+1):
            if (x & (x-1)) == 0:
                shift += 1
            soln <<= shift
            soln |= x
            soln %= MOD
        return soln



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