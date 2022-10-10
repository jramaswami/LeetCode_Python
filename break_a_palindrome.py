"""
LeetCode :: October 2022 Challenge :: Break a Palindrome
jramaswami
"""


class Solution:

    def breakPalindrome(self, palindrome):
        # Corner case: you cannot make a 1 letter word /not/ a palindrome.
        if len(palindrome) < 2:
            return ""

        # We want to lower the first letter that we can but this excludes
        # the middle letter of an odd length palindrome because that won't
        # actually break the palindrome.
        mid = -1
        if len(palindrome) % 2:
            mid = len(palindrome) // 2
        print(palindrome, len(palindrome), mid)
        for i, c in enumerate(palindrome):
            if i != mid and palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        # If we have reached this point then all the changeable letters are
        # 'a', so we must change the last to b.
        return palindrome[:-1] + 'b'


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
