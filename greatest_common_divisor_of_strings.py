"""
LeetCode
1071. Greatest Common Divisor of Strings
February 2023 Challenge
jramaswami
"""


from typing import *



class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def divides_s(s, t):
            "Return True if t 'divides' s."
            if len(s) % len(t) == 0:
                d = len(s) // len(t)
                return s == (t * d)
            return False

        for k in range(1, min(len(str1), len(str2)) + 1):
            if len(str1) % k == 0 and len(str2) % k  == 0 and str1[:k] == str2[:k]:
                t = str1[:k]
                if divides_s(str1, t) and divides_s(str2, t):
                    return t
        return ""


def test_1():
    str1 = "ABCABC"
    str2 = "ABC"
    expected = "ABC"
    assert Solution().gcdOfStrings(str1, str2) == expected


def test_2():
    str1 = "ABABAB"
    str2 = "ABAB"
    expected = "AB"
    assert Solution().gcdOfStrings(str1, str2) == expected


def test_3():
    str1 = "LEET"
    str2 = "CODE"
    expected = ""
    assert Solution().gcdOfStrings(str1, str2) == expected



def test_4():
    "WA"
    str1 = "ABABABAB"
    str2 = "ABAB"
    expected = "ABAB"
    assert Solution().gcdOfStrings(str1, str2) == expected
