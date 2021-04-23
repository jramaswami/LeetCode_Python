"""
Leet Code :: April 2021 Challenge :: Count Binary Substrings
jramaswami
"""
from typing import *


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        soln = 0
        curr = "x"
        left = 0
        prev_left = 0
        curr_count = 0
        other_count = 0
        for i, c in enumerate(s):
            if c == curr:
                curr_count += 1
                if curr_count <= other_count:
                    soln += 1
            else:
                curr = c
                prev_left, left = left, i
                curr_count, other_count = 1, curr_count
                if curr_count <= other_count:
                    soln += 1

        return soln


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