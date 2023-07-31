"""
LeetCode
712. Minimum ASCII Delete Sum for Two Strings
July 2023 Challenge
jramaswami
"""


import functools


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        INF = pow(10, 20)

        @functools.cache
        def rec(i, j):
            # Base Cases
            if i >= len(s1) and j >= len(s2):
                return 0
            if i >= len(s1):
                return ord(s2[j]) + rec(i, j+1)
            if j >= len(s2):
                return ord(s1[i]) + rec(i+1, j)

            result = INF
            # Keep the same
            if s1[i] == s2[j]:
                result = min(result, rec(i+1, j+1))
            # Delete s1[i]
            result = min(result, ord(s1[i]) + rec(i+1, j))
            # Delete s2[j]
            result = min(result, ord(s2[j]) + rec(i, j+1))
            return result

        return rec(0, 0)


def test_1():
    s1 = "sea"
    s2 = "eat"
    expected = 231
    assert Solution().minimumDeleteSum(s1, s2) == expected


def test_2():
    s1 = "delete"
    s2 = "leet"
    expected = 403
    assert Solution().minimumDeleteSum(s1, s2) == expected