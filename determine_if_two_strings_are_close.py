"""
LeetCode :: 1657. Determine if Two Strings Are Close
December 2022 Challenge
jramaswami
"""


import collections


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freqs1 = collections.Counter(word1)
        freqs2 = collections.Counter(word2)
        return (
            set(freqs1.values()) == set(freqs2.values()) and
            set(freqs1.keys()) == set(freqs2.keys())
        )



def test_1():
    word1 = "abc"
    word2 = "bca"
    expected = True
    assert Solution().closeStrings(word1, word2) == expected


def test_2():
    word1 = "a"
    word2 = "aa"
    expected = False
    assert Solution().closeStrings(word1, word2) == expected


def test_3():
    word1 = "cabbba"
    word2 = "abbccc"
    expected = True
    assert Solution().closeStrings(word1, word2) == expected


def test_4():
    "WA"
    word1 = "uau"
    word2 = "ssx"
    expected = False
    assert Solution().closeStrings(word1, word2) == expected


def test_5():
    "WA"
    word1 = "aaabbbbccddeeeeefffff"
    word2 = "aaaaabbcccdddeeeeffff"
    expected = False
    assert Solution().closeStrings(word1, word2) == expected