"""
LeetCode :: July 2022 Challenge :: 242. Valid Anagram
jramaswami
"""


import collections


class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)


def test_1():
    s = "anagram"
    t = "nagaram"
    expected = True
    assert Solution().isAnagram(s, t) == expected


def test_2():
    s = "rat"
    t = "car"
    expected = False
    assert Solution().isAnagram(s, t) == expected