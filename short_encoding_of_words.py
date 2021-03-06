"""
LeetCode :: March 2021 Challenge :: Short Encoding of Words
jramaswami
"""
from typing import *


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words0 = sorted(words, key=len, reverse=True)
        encoding = []
        for wd in words0:
            encode_this = True
            for enc in encoding:
                if enc.count(wd):
                    encode_this = False
                    break
            if encode_this:
                encoding.append(wd)

        return sum(len(e) for e in encoding) + len(encoding)
        

def test_1():
    words = ["bell", "time", "me"]
    assert Solution().minimumLengthEncoding(words) == 10

def test_2():
    words = ["t"]
    assert Solution().minimumLengthEncoding(words) == 2

def test_3():
    words = ["feipyxx", "e"]
    assert Solution().minimumLengthEncoding(words) == 10
