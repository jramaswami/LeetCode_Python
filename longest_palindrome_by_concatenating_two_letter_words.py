"""
LeetCode :: 2131. Longest Palindrome by Concatenating Two Letter Words
November 2022 Challenge
jramaswami
"""


from typing import *


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        same_letter_pair = 0
        two_letter_pairs = 0
        ord_a = ord('a')
        pair_matrix = [[False for _ in range(26)] for _ in range(26)]
        for x, y in words:
            i = ord(x) - ord_a
            j = ord(y) - ord_a
            if i == j:
                same_letter_pair = 1
            else:
                if pair_matrix[i][j] == False and pair_matrix[j][i] == True:
                    two_letter_pairs += 1
            pair_matrix[i][j] = True
        return 2 * ((2 * two_letter_pairs) + same_letter_pair)


def test_1():
    words = ["lc","cl","gg"]
    expected = 6
    assert Solution().longestPalindrome(words) == expected


def test_2():
    words = ["ab","ty","yt","lc","cl","ab"]
    expected = 8
    assert Solution().longestPalindrome(words) == expected


def test_3():
    words = ["cc","ll","xx"]
    expected = 2
    assert Solution().longestPalindrome(words) == expected


def test_4():
    "WA"
    words = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]
    expected = 22
    assert Solution().longestPalindrome(words) == expected