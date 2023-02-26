"""
LeetCode :: 72. Edit Distance
jramaswami
"""


import math
import functools


class Solution:

    def minDistance(self, word1, word2):
        @functools.cache
        def rec(i, j):
            if i >= len(word1):
                return len(word2) - j
            if j >= len(word2):
                return len(word1) - i

            result = math.inf
            if word1[i] == word2[j]:
                result = min(result, rec(i+1, j+1))
            else:
                # Make them the same letter.
                result = min(result, 1 + rec(i+1, j+1))
            # Delete word1[i] or insert into word2
            result = min(result, 1 + rec(i+1, j))
            # Delete word2[j] or insert into word1
            result = min(result, 1 + rec(i, j+1))
            return result

        return rec(0, 0)


def test_1():
    word1 = "horse"
    word2 = "ros"
    expected = 3
    assert Solution().minDistance(word1, word2) == expected


def test_2():
    word1 = "intention"
    word2 = "execution"
    expected = 5
    assert Solution().minDistance(word1, word2) == expected


def test_3():
    "RTE"
    word1 = ""
    word2 = ""
    expected = 0
    assert Solution().minDistance(word1, word2) == expected


def test_4():
    "WA"
    word1 = "a"
    word2 = "b"
    expected = 1
    assert Solution().minDistance(word1, word2) == expected
