"""
LeetCode :: April 2021 Challenge :: Verifying an Alien Dictionary
jramaswami
"""
from typing import *


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        encoding = dict((c, i) for i, c in enumerate(order))
        encoded_words = [[encoding[c] for c in wd] for wd in words]
        return all(a <= b for a, b in zip(encoded_words[:-1], encoded_words[1:]))


def test_1():
    words = ["hello","leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    assert Solution().isAlienSorted(words, order) == True

def test_2():
    words = ["word","world","row"]
    order = "worldabcefghijkmnpqstuvxyz"
    assert Solution().isAlienSorted(words, order) == False

def test_3():
    words = ["apple","app"]
    order = "abcdefghijklmnopqrstuvwxyz"
    assert Solution().isAlienSorted(words, order) == False
