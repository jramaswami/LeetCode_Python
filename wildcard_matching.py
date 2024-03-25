"""
LeetCode
44. Wildcard Matching
jramaswami
"""


import functools


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @functools.cache
        def rec(i: int, j: int) -> bool:
            if i >= len(s) and j >= len(p):
                return True
            if i >= len(s):
                return False
            if j >= len(p):
                return False

            result = False
            if p[j] == '*':
                result = result or rec(i+1, j+1)
                result = result or rec(i, j+1)
                result = result or rec(i+1, j)
            elif p[j] == '?' or s[i] == p[j]:
                result = result or rec(i+1, j+1)
            return result

        return rec(0, 0)


def test_1():
    s = "aa"
    p = "a"
    expected = False
    assert Solution().isMatch(s, p) == expected


def test_2():
    s = "aa"
    p = "*"
    expected = True
    assert Solution().isMatch(s, p) == expected


def test_3():
    s = "aa"
    p = "a"
    expected = False
    assert Solution().isMatch(s, p) == expected


def test_4():
    "WA"
    s = ""
    p = "******"
    expected = True
    assert Solution().isMatch(s, p) == expected

