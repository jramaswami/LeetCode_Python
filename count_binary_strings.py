"""
Leet Code :: April 2021 Challenge :: Count Binary Substrings
jramaswami
"""
from typing import *
from itertools import groupby


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        soln = 0
        groups = [sum(1 for _ in g) for k, g in groupby(s)]
        return sum(min(a, b) for a, b in zip(groups[:-1], groups[1:]))


def test_1():
    s = "00110011"
    expected = 6
    assert Solution().countBinarySubstrings(s) == expected


def test_2():
    s = "10101"
    expected = 4
    assert Solution().countBinarySubstrings(s) == expected


def test_3():
    s = ""
    expected = 0
    assert Solution().countBinarySubstrings(s) == expected


def test_4():
    s = "100110001001011011100101"
    expected = 17
    assert Solution().countBinarySubstrings(s) == expected


def test_5():
    s = "11011111000011001011101101101"
    expected = 19
    assert Solution().countBinarySubstrings(s) == expected


def test_6():
    s = "1011011101000110111110110001111100110101111110"
    expected = 27
    assert Solution().countBinarySubstrings(s) == expected