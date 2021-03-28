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
        words = ["zero", "two", "four", "six", "eight", "seven", "five", "three", "one", "nine"]
        keyletters = ["z", "w", "u", "x", "g", "s", "v", "t", "o", "i"]
        digits = ["0", "2", "4", "6", "8", "7", "5", "3", "1", "9"]
        soln = []
        for word, keyletter, digit in zip(words, keyletters, digits):
            min_freq = ctr[keyletter]
            for c in word:
                ctr[c] -= min_freq
            soln.append(digit * min_freq)
        return "".join(sorted(soln))


def test_1():
    assert Solution().originalDigits("owoztneoer") == "012"

def test_2():
    assert Solution().originalDigits("fviefuro") == "45"

def test_3():
    assert Solution().originalDigits("zeroonetwothreefourfivesixseveneightnine") == "0123456789"

# z {'zero'}
# e {'five', 'seven', 'nine', 'zero', 'one', 'eight', 'three'}
# r {'four', 'three', 'zero'}
# o {'one', 'four', 'two', 'zero'}
# n {'one', 'seven', 'nine'}
# t {'eight', 'three', 'two'}
# w {'two'}
# h {'eight', 'three'}
# f {'four', 'five'}
# u {'four'}
# i {'eight', 'six', 'five', 'nine'}
# v {'five', 'seven'}
# s {'six', 'seven'}
# x {'six'}
# g {'eight'}

