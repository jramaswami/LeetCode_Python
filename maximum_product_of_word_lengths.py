"""
LeetCode :: May 2021 Challenge :: Maximum Product of Word Lengths
jramaswami
"""


from typing import *
from itertools import combinations
from collections import namedtuple


Word = namedtuple('Word', ['letters', 'length'])


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        soln = 0
        # O(N * word length)
        words0 = [Word(set(w), len(w)) for w in words]
        # O(N^2)
        for a, b in combinations(words0, 2):
            if a.letters.isdisjoint(b.letters):
                soln = max(soln, a.length * b.length)
        return soln


def test_1():
    words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    expected = 16
    assert Solution().maxProduct(words) == expected


def test_2():
    words = ["a","ab","abc","d","cd","bcd","abcd"]
    expected = 4
    assert Solution().maxProduct(words) == expected


def test_3():
    words = ["a","aa","aaa","aaaa"]
    expected = 0
    assert Solution().maxProduct(words) == expected