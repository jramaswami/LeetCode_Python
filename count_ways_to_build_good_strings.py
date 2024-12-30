"""
LeetCode
2466. Count Ways To Build Good Strings
December 2024 Challenge
jramaswami
"""


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = pow(10, 9) + 7
        dp = [0 for _ in range(high+1)]
        dp[0] = 1
        for n in range(high):
            if n + zero <= high:
                dp[n + zero] = (dp[n + zero] + dp[n]) % MOD
            if n + one <= high:
                dp[n + one] = (dp[n + one] + dp[n]) % MOD

        soln = 0
        for n in range(low, high+1):
            soln = (soln + dp[n]) % MOD
        return soln % MOD


def test_1():
    low = 3
    high = 3
    zero = 1
    one = 1
    expected = 8
    assert Solution().countGoodStrings(low, high, zero, one) == expected


def test_2():
    low = 2
    high = 3
    zero = 1
    one = 2
    expected = 5
    assert Solution().countGoodStrings(low, high, zero, one) == expected
