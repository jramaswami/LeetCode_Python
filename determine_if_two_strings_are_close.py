"""
LeetCode :: 1657. Determine if Two Strings Are Close
December 2022 Challenge
jramaswami
"""


import collections


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # You can swap letters any way you want, so the order does not matter.
        # You can swap the group frequencies as well, so the order of frequency
        # does not matter either.  You must have the same frequencies and the
        # same letters in both words.
        freqs1 = collections.Counter(word1)
        freqs2 = collections.Counter(word2)
        return (
            sorted(freqs1.values()) == sorted(freqs2.values()) and
            set(word1) == set(word2)
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