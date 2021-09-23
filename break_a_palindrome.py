"""
LeetCode :: September 2021 Challenge :: Break a Palindrome
jramaswami
"""


class Solution:

    def breakPalindrome(self, palindrome):
        # Corner case: you cannot alter a palindrome of a single letter to make
        # it lexicographically smaller non-palindrome.
        if len(palindrome) <= 1:
            return ""
        P = list(palindrome)
        mid = len(P) // 2
        if len(P) % 2 == 0:
            mid += 1
        # Find the first letter you can reduce.
        for i, char in enumerate(P[:mid]):
            if char != 'a':
                P[i] = 'a'
                return "".join(P)
        # If you didn't find a reducible letter, find the last
        # letter you can increase by one.  This should be the
        # last letter in the palindrome.
        P[-1] = chr(ord(P[-1]) + 1)
        return "".join(P)



def test_1():
    palindrome = "abccba"
    expected = "aaccba"
    assert Solution().breakPalindrome(palindrome) == expected


def test_2():
    palindrome = "a"
    expected = ""
    assert Solution().breakPalindrome(palindrome) == expected


def test_3():
    palindrome = "aa"
    expected = "ab"
    assert Solution().breakPalindrome(palindrome) == expected


def test_4():
    palindrome = "aba"
    expected = "abb"
    assert Solution().breakPalindrome(palindrome) == expected


def test_5():
    palindrome = "aaaxaaa"
    expected = "aaaxaab"
    assert Solution().breakPalindrome(palindrome) == expected
