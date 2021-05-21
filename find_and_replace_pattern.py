"""
LeetCode :: May 2021 Challenge :: Find and Replace Pattern
jramaswami
"""
from typing import *


def transform(word):
    """Transform word into pattern."""
    code = dict()
    T = []
    for i, c in enumerate(word):
        if c in code:
            T.append(code[c])
        else:
            code[c] = i
            T.append(i)
    return T


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        soln = []
        pattern_t = transform(pattern)
        for word in words:
            if pattern_t == transform(word):
                soln.append(word)
        return soln



def test_1():
    words = ["abc","deq","mee","aqq","dkd","ccc"]
    pattern = "abb"
    expected = ["mee","aqq"]
    assert Solution().findAndReplacePattern(words, pattern) == expected


def test_2():
    words = ["a","b","c"]
    pattern = "a"
    expected = ["a","b","c"]
    assert Solution().findAndReplacePattern(words, pattern) == expected
