"""
LeetCode :: August 2022 Challenge :: 387. First Unique Character in a String
jramaswami
"""


import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        freqs = collections.Counter(s)
        for i, c in enumerate(s):
            if freqs[c] == 1:
                return i
        return -1


def test_1():
    s = "leetcode"
    expected = 0
    assert Solution().firstUniqChar(s) == expected


def test_2():
    s = "loveleetcode"
    expected = 2
    assert Solution().firstUniqChar(s) == expected


def test_3():
    s = "aabb"
    expected = -1
    assert Solution().firstUniqChar(s) == expected