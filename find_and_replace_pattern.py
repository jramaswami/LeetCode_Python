"""
LeetCode :: July 2022 Challenge :: Find and Replace Pattern
jramaswami
"""


from typing import *


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        def matches(word, pattern):
            if len(pattern) != len(word):
                return False
            pattern_to_word = dict()
            word_to_pattern = dict()
            for p, w in zip(pattern, word):
                # If this is the first time for both, then place edge
                # between two letters.
                if p not in pattern_to_word and w not in word_to_pattern:
                    pattern_to_word[p] = w
                    word_to_pattern[w] = p
                else:
                    if pattern_to_word.get(p, '?') != w or word_to_pattern.get(w, '?') != p:
                        return False
            return True

        return [wd for wd in words if matches(wd, pattern)]


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