"""
LeetCode :: April 2021 Challenge :: Determine if String Halves Are Alike
jramaswami
"""
from typing import *


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left = 0
        right = 0
        mid = len(s) // 2
        for i, c in enumerate(s):
            if c in vowels:
                if i < mid:
                    left += 1
                else:
                    right += 1

        return left == right


def test_1():
    assert Solution().halvesAreAlike("book") == True

def test_2():
    assert Solution().halvesAreAlike("textbook") == False

def test_3():
    assert Solution().halvesAreAlike("MerryChristmas") == False

def test_4():
    assert Solution().halvesAreAlike("AbCdEfGh") == True


