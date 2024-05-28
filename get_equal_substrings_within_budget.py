"""
LeetCode
1208. Get Equal Substrings Within Budget
May 2024 Challenge
jramaswami
"""


import functools


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        def rec(i, cost):
            if i >= len(s):
                return 0

            if s[i] == t[i]:
                return 1 + rec(i+1, cost)
            else:
                x = abs(ord(s[i]) - ord(t[i]))
                if x + cost <= maxCost:
                    return 1 + rec(i, x + cost)
            return 0

        return rec(0, 0)



def test_1():
    s = "abcd"
    t = "bcdf"
    maxCost = 3
    expected = 3
    result = Solution().equalSubstring(s, t, maxCost)
    assert result == expected


def test_2():
    s = "abcd"
    t = "cdef"
    maxCost = 3
    expected = 1
    result = Solution().equalSubstring(s, t, maxCost)
    assert result == expected


def test_3():
    s = "abcd"
    t = "acde"
    maxCost = 0
    expected = 1
    result = Solution().equalSubstring(s, t, maxCost)
    assert result == expected


def test_4():
    "WA"
    s = "krrgw"
    t = "zjxss"
    maxCost = 19
    expected = 2
    result = Solution().equalSubstring(s, t, maxCost)
    assert result == expected
