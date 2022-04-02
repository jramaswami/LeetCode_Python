"""
LeetCode :: April 2022 Challenge :: 680. Valid Palindrome II
jramaswami
"""


class Solution:
    def validPalindrome(self, S):
        def valid(left, right):
            while left < right:
                if S[left] != S[right]:
                    return False
                left += 1
                right -= 1
            return True

        def valid_but_one(left, right):
            while left < right:
                if S[left] != S[right]:
                    return (valid(left+1, right) or valid(left, right-1))
                left += 1
                right -= 1
            return True

        return valid_but_one(0, len(S)-1)


def test_1():
    S = "aba"
    expected = True
    assert Solution().validPalindrome(S) == expected


def test_2():
    S = "abca"
    expected = True
    assert Solution().validPalindrome(S) == expected


def test_3():
    S = "abc"
    expected = False
    assert Solution().validPalindrome(S) == expected
