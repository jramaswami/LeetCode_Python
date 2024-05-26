"""
LeetCode
552. Student Attendance Record II
May 2024 Challenge
jramaswami
"""


import functools


class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = pow(10, 9) + 7

        @functools.cache
        def rec(i, a, l):
            if i == 0:
                return 1

            # Present
            result = rec(i-1, a, 0)
            # Absent
            if a == 0:
                result += rec(i-1, a+1, 0)
                result %= MOD
            # Late
            if l < 2:
                result += rec(i-1, a, l+1)
                result %= MOD

            return result % MOD

        return rec(n, 0, 0)


import sys
sys.setrecursionlimit(pow(10, 6))


def test_1():
    assert Solution().checkRecord(2) == 8


def test_2():
    assert Solution().checkRecord(1) == 3


def test_3():
    assert Solution().checkRecord(10101) == 183236316


def test_4():
    "MLE"
    assert Solution().checkRecord(99995) == 0