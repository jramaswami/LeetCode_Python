"""
LeetCode
3333. Find the Original Typed String II
July 2025 Challenge
jramaswami

REF: https://www.youtube.com/watch?v=CymJVoz7XSY
"""


import itertools


class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = pow(10, 9) + 7

        # Group by letter
        LETTER, COUNT = 0, 1
        groups = []
        P = 1
        for letter in word:
            if not groups or groups[-1][LETTER] != letter:
                groups.append([letter, 1])
            else:
                groups[-1][COUNT] += 1

        P = 1
        for g in groups:
            P *= g[COUNT]
            P %= MOD

        if k <= len(groups):
            return P

        # dp[number of groups][length up to k-1] = number of ways
        dp = [[0 for _ in range(k)] for _ in range(len(groups)+1)]
        dp[0][0] = 1
        for i in range(1, len(groups)+1):
            prefix = list(itertools.accumulate(dp[i-1]))
            for j in range(1,k):
                left = j - 1 - groups[i-1][COUNT]
                x = prefix[j-1]
                if left >= 0:
                    x -= prefix[left]
                dp[i][j] += x
                dp[i][j] %= MOD
        return (P - sum(dp[-1])) % MOD


def test_1():
    word = "aabbccdd"
    k = 7
    expected = 5
    assert Solution().possibleStringCount(word, k) == expected


def test_2():
    word = "aabbccdd"
    k = 8
    expected = 1
    assert Solution().possibleStringCount(word, k) == expected


def test_3():
    word = "aaabbb"
    k = 3
    expected = 8
    assert Solution().possibleStringCount(word, k) == expected