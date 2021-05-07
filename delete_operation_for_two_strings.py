"""
Leet Code :: May 2021 Challenge :: Delete Operation for Two Strings
jramaswami
"""
from typing import *
from collections import Counter


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Compute longest common subsequence.  The remove letter the number of
        letters from each word to make it the longest common subsequence.
        """

        def get(i, j, dp):
            """Convenience method that returns 0 if you go out of bounds on dp."""
            if i < 0:
                return 0
            if j < 0:
                return 0
            return dp[i][j]

        dp = [[0 for _ in word2] for _ in word1]
        lcs = 0
        for i, c1 in enumerate(word1):
            for j, c2 in enumerate(word2):
                if c1 == c2:
                    dp[i][j] = get(i-1, j-1, dp) + 1
                else:
                    dp[i][j] = max(get(i-1, j, dp), get(i, j-1, dp))
                lcs = max(dp[i][j], lcs)

        return (len(word1) - lcs) + (len(word2) - lcs)


def test_1():
    word1 = "sea"
    word2 = "eat"
    assert Solution().minDistance(word1, word2) == 2


def test_2():
    word1 = "leetcode"
    word2 = "etco"
    assert Solution().minDistance(word1, word2) == 4


def test_3():
    """WA"""
    word1 = "sea"
    word2 = "ate"
    assert Solution().minDistance(word1, word2) == 4


def test_4():
    word1 = "yqeoiryeuyeiuoadfuiaydfuiyasdfiouyfduiyaiusodioasudfyoiauyf"
    word2 = "qwoieruqowreuoqpwreuoiqwrepqoweurpoaufpouafpoiausfoiu"
    assert Solution().minDistance(word1, word2) == 62