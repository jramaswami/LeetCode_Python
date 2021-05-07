"""
Leet Code :: May 2021 Challenge :: Delete Operation for Two Strings
jramaswami
"""
from typing import *
from math import inf


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Compute longest common subsequence.  The remove letter the number of
        letters from each word to make it the longest common subsequence.
        """

        def min_dist(index1, index2):
            """
            Return the minimum distance between word1[index:] and word2[index:]
            """
            if index1 == len(word1) and index2 == len(word2):
                # We have reached the end
                return 0

            if index1 == len(word1):
                # We can only delete from word2
                return 1 + min_dist(index1, index2 + 1)

            if index2 == len(word2):
                # We can only delete from word1
                return 1 + min_dist(index1 + 1, index2)

            if word1[index1] == word2[index2]:
                # We do not have to delete from either word.
                return min_dist(index1 + 1, index2 + 1)

            mn = inf
            # Delete from word 1
            mn = min(mn, 1 + min_dist(index1 + 1, index2))
            # Delete from word2
            mn = min(mn, 1 + min_dist(index1, index2+1))
            return mn

        return min_dist(0, 0)


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