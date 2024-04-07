"""
LeetCode
678. Valid Parenthesis String
April 2024 Challenge
jramaswami
"""


import functools


class Solution:
    def checkValidString(self, s: str)  -> bool:

        @functools.cache
        def rec(i, acc):
            if acc < 0:
                return False

            if i >= len(s):
                return acc == 0

            if s[i] == '(':
                return rec(i+1, acc+1)
            elif s[i] == ')':
                return rec(i+1, acc-1)
            else:
                return (
                    rec(i+1, acc) or
                    rec(i+1, acc-1) or
                    rec(i+1, acc+1)
                )

        return rec(0, 0)


def test_1():
    s = "()"
    expected = True
    assert Solution().checkValidString(s) == expected


def test_2():
    s = "(*)"
    expected = True
    assert Solution().checkValidString(s) == expected


def test_3():
    s = "(*))"
    expected = True
    assert Solution().checkValidString(s) == expected
