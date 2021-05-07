"""
Leet Code :: May 2021 Challenge :: Delete Operation for Two Strings
jramaswami
"""
from typing import *
from collections import Counter


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ctr1 = Counter(word1)
        ctr2 = Counter(word2)
        intersection = ctr1 & ctr2
        return sum((ctr1-intersection).values()) + sum((ctr2 - intersection).values())


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
    word2 = "eat"
    assert Solution().minDistance(word1, word2) == 4