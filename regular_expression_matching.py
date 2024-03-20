"""
LeetCode
10. Regular Expression Matching
jramaswami
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def rec(i, j):
            # If both pointers are done, we have a match.
            if i >= len(s) and j >= len(p):
                return True

            # If only one pointer is done, we do not have a match.
            if i >= len(s) or j >= len(p):
                return False

            if p[j] == '*':
                # We match and we can choose to move j or stay
                return rec(i+1, j) or rec(i+1, j+1)
            elif p[j] == '.':
                # We match
                return rec(i+1, j+1)

            return s[i] == p[j] and rec(i+1, j+1)

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
    expected = True
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