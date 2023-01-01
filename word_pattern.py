"""
LeetCode
290. Word Pattern
January 2023 Challenge
jramaswami
"""


from typing import *


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        tokens = s.split()
        if len(tokens) != len(pattern):
            return False

        pattern_visited = dict()
        token_visited = dict()
        for p, t in zip(pattern, tokens):
            if p in pattern_visited and t != pattern_visited[p]:
                return False
            if t in token_visited and p != token_visited[t]:
                return False
            pattern_visited[p] = t
            token_visited[t] = p
        return True


def test_1():
    pattern = "abba"
    s = "dog cat cat dog"
    assert Solution().wordPattern(pattern, s) == True


def test_2():
    pattern = "abba"
    s = "dog cat cat fish"
    assert Solution().wordPattern(pattern, s) == False


def test_3():
    pattern = "aaaa"
    s = "dog cat cat dog"
    assert Solution().wordPattern(pattern, s) == False


def test_4():
    "WA"
    pattern = "abba"
    s = "dog dog dog dog"
    assert Solution().wordPattern(pattern, s) == False


def test_5():
    "WA"
    pattern = "aaa"
    s = "aa aa aa aa"
    assert Solution().wordPattern(pattern, s) == False

