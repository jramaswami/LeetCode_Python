"""
LeetCode
10. Regular Expression Matching
jramaswami
"""


import enum
import collections
from typing import List


MatchElement = collections.namedtuple('MatchElement', ['character', 'quantifier'])


class Quantifier(enum.Enum):
    Single = enum.auto()
    Any = enum.auto()


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        match_pattern: List[MatchElement] = []
        i = 0
        while i < len(p):
            char = p[i]
            quantifier = Quantifier.Single
            if i + 1 < len(p) and p[i + 1] == '*':
                quantifier = Quantifier.Any
                i += 1
            match_pattern.append(MatchElement(char, quantifier))
            i += 1

        def rec(i, j):
            # If both pointers are done, we have a match.
            if i >= len(s) and j >= len(match_pattern):
                return True

            # If only one pointer is done, we do not have a match.
            if i >= len(s) or j >= len(match_pattern):
                return False

            result = False

            if match_pattern[j].quantifier == Quantifier.Any:
                if s[i] ==  match_pattern[j].character or match_pattern[j].character == '.':
                    result = result or rec(i+1, j)
                    result = result or rec(i+1, j+1)
                else:
                    result = result or rec(i, j+1)
            elif s[i] == match_pattern[j].character or match_pattern[j].character == '.':
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
    p = "a*"
    expected = True
    assert Solution().isMatch(s, p) == expected


def test_3():
    s = "ab"
    p = ".*"
    expected = True
    assert Solution().isMatch(s, p) == expected


def test_4():
    s = 'abcda'
    p = 'ab*a'
    expected = False
    assert Solution().isMatch(s, p) == expected


def test_5():
    s = 'abcda'
    p = 'ab.a'
    expected = False
    assert Solution().isMatch(s, p) == expected


def test_6():
    "WA: * means any number of preceding character, not any number of characters"
    s = 'aab'
    p = 'c*a*b'
    expected = True
    assert Solution().isMatch(s, p) == expected


def test_7():
    "WA"
    s = "mississippi"
    p = "mis*is*p*."
    expected = False
    assert Solution().isMatch(s, p) == expected


def test_8():
    "WA: need to handle *'s after reaching the end of s"
    s = "a"
    p = "ab*"
    expected = True
    assert Solution().isMatch(s, p) == expected