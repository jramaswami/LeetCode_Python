"""
LeetCode
459. Repeated Substring Pattern
August 2023 Challenge
jramaswami
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Simplest possible solution
        for length in range(1, len(s)):
            q, r = divmod(len(s), length)
            if r == 0:
                t = s[:length]
                if t * q == s:
                    return True
        return False


def test_1():
    s = "abab"
    expected = True
    assert Solution().repeatedSubstringPattern(s) == expected


def test_2():
    s = "aba"
    expected = False
    assert Solution().repeatedSubstringPattern(s) == expected


def test_3():
    s = "abcabcabcabc"
    expected = True
    assert Solution().repeatedSubstringPattern(s) == expected


def test_4():
    "WA"
    s = "bb"
    expected = True
    assert Solution().repeatedSubstringPattern(s) == expected