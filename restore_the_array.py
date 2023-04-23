"""
LeetCode
1416. Restore the Array
April 2023 Challenge
jramaswami
"""


import functools


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = pow(10, 9) + 7

        @functools.cache
        def rec(index, currnum):
            # Base cases.
            if currnum > k:
                return 0

            if index >= len(s):
                if currnum > 0:
                    return 1
                return 0

            digit = int(s[index])
            # No leading zeros
            if currnum == 0 and digit == 0:
                return 0

            result = 0
            if currnum > 0:
                # We could emit a number before the current digit.
                result += rec(index+1, digit)
                result %= MOD

            # We could append the current digit to the current number.
            result += rec(index+1, (currnum * 10) + digit)
            result %= MOD

            return result % MOD

        return rec(0, 0) % MOD


def test_1():
    s = "1000"
    k = 10000
    expected = 1
    assert Solution().numberOfArrays(s, k) == expected


def test_2():
    s = "1000"
    k = 10
    expected = 0
    assert Solution().numberOfArrays(s, k) == expected


def test_3():
    s = "1317"
    k = 2000
    expected = 8
    assert Solution().numberOfArrays(s, k) == expected


def test_4():
    "WA"
    s = "2020"
    k = 30
    expected = 1
    assert Solution().numberOfArrays(s, k) == expected
