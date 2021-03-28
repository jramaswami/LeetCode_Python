"""
LeetCode :: March 2021 Challenge :: Reconstruct Original Digits from English
jramaswami
"""
from typing import *
from collections import Counter
from math import inf


class Solution:
    def originalDigits(self, s: str) -> str:
        ctr = Counter(s)
        words = ["zero", "one", "two", "three", "four", "five", "six",
                 "seven", "eight", "nine"]
        digits = "0123456789"
        soln = []
        for word, digit in zip(words, digits):
            min_freq = inf
            for c in word:
                min_freq = min(ctr[c], min_freq)
            for c in word:
                ctr[c] -= min_freq
            soln.append(digit * min_freq)
        return "".join(soln)


def test_1():
    assert Solution().originalDigits("owoztneoer") == "012"

def test_2():
    assert Solution().originalDigits("fviefuro") == "45"

def test_3():
    assert Solution().originalDigits("zeroonetwothreefourfivesixseveneightnine") == "0123456789"
