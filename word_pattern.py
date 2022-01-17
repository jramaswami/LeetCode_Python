"""
LeetCode :: January 2022 Challenge :: 290. Word Pattern
jramaswami
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        visited_pattern = dict()
        visited_word = dict()
        tokens = s.strip().split()
        if len(pattern) != len(tokens):
            return False
        for p, w in zip(pattern, tokens):
            if p in visited_pattern and  w != visited_pattern[p]:
                return False
            if w in visited_word and visited_word[w] != p:
                return False
            visited_pattern[p] = w
            visited_word[w] = p
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

