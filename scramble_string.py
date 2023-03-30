"""
LeetCode
87. Scramble String
March 2023 Challenge
jramaswami
"""


import collections
import functools
from typing import *


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @functools.cache
        def rec(left1, right1, left2, right2):
            if left1 == right1:
                return s1[left1] == s2[left2]

            for i in range(right1 - left1):
                if rec(left1, left1+i, left2, left2+i) and rec(left1+i+1, right1, left2+i+1, right2):
                    return True
                if rec(left1, left1+i, right2-i, right2) and rec(left1+i+1, right1, left2, right2-i-1):
                    return True
            return False

        return rec(0, len(s1)-1, 0, len(s2)-1)


def test_1():
    s1 = "great"
    s2 = "rgeat"
    expected = True
    assert Solution().isScramble(s1, s2) == expected
