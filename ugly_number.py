"""
LeetCode :: 263. Ugly Number
November 2022 Challenge
jramaswami
"""


class Solution:

    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False

        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p
        if n == 1:
            return True
        return False


def test_1():
    n = 6
    expected = True
    assert Solution().isUgly(n) == expected


def test_2():
    n = 1
    expected = True
    assert Solution().isUgly(n) == expected


def test_3():
    n = 14
    expected = False
    assert Solution().isUgly(n) == expected


def test_4():
    "TLE: endless loop."
    n = 0
    expected = False
    assert Solution().isUgly(n) == expected
