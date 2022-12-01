"""
LeetCode :: Determine if String Halves Are Alike
November 2022 Challenge
jramaswami
"""


from typing import *


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = 'aeiouAEIOU'
        mid = len(s) // 2
        left_vowels = sum(c in vowels for c in s[:mid])
        right_vowels = sum(c in vowels for c in s[mid:])
        return left_vowels == right_vowels


def test_1():
    assert Solution().halvesAreAlike("book") == True

def test_2():
    assert Solution().halvesAreAlike("textbook") == False

def test_3():
    assert Solution().halvesAreAlike("MerryChristmas") == False

def test_4():
    assert Solution().halvesAreAlike("AbCdEfGh") == True


