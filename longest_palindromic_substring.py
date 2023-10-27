"""
LeetCode
5. Longest Palindromic Substring
October 2023 Challenge
jramaswami
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        soln = s[-1]
        if len(s) == 1:
            return s
        #dp[length][i] = string starting at i is palindrome up to length
        dp = [[False for _ in s] for _ in range(len(s)+1)]
        # All strings of length 1 are palindromes
        dp[1] = [True for _ in s]
        # Strings of length 2 are palindromes if the two letters are equal
        for i, _ in enumerate(dp[2][:-1]):
            if s[i] == s[i+1]:
                dp[2][i] = True
                soln = s[i:i+2]

        for l in range(3, len(s)+1):
            for i in range(0, len(s)-l+1):
                # A palindrome starting at index i of length l is a a palindrome
                # if s[i] and s[i+l-1] are the same and dp[i+1][l-2] is a palindrome
                if s[i] == s[i+l-1] and dp[i+1][l-2]:
                    dp[i][l] = True
                    soln = s[i:i+l]

        return soln


def test_1():
    s = "babad"
    expected = "bab"
    assert Solution().longestPalindrome(s) == expected


def test_2():
    s = "cbbd"
    expected = "bb"
    assert Solution().longestPalindrome(s) == expected


def test_3():
    "RTE"
    s = "ccc"
    expected = "ccc"
    assert Solution().longestPalindrome(s) == expected