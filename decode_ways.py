"""
LeetCode :: October 2022 Challenge :: Decode Ways
jramaswami
"""


import functools


class Solution:
    def numDecodings(self, s: str) -> int:
        t = [int(x) for x in s]

        @functools.cache
        def rec(i):
            # Base Case.
            if i >= len(t):
                return 1

            # Prune
            # No leading or single zeros allowed
            if t[i] == 0:
                return 0

            # Compute.
            single = rec(i+1)
            double = 0
            if i + 1 < len(t) and 0 < (t[i] * 10) + t[i+1] <= 26:
                double = rec(i+2)
            return single + double

        return rec(0)




def test_1():
    s = "12"
    expected = 2
    assert Solution().numDecodings(s) == expected


def test_2():
    s = "226"
    expected = 3
    assert Solution().numDecodings(s) == expected


def test_3():
    s = "06"
    expected = 0
    assert Solution().numDecodings(s) == expected


def test_4():
    "WA"
    s = "27"
    expected = 1
    assert Solution().numDecodings(s) == expected