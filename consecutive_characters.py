"""
LeetCode :: December 2021 Challenge :: 1446. Consecutive Characters
jramaswami
"""


import itertools


class Solution:
    def maxPower(self, S):
        return max(sum(1 for c in g) for _, g in itertools.groupby(S))


def test_1():
    s = "leetcode"
    assert Solution().maxPower(s) == 2


def test_2():
    s = "abbcccddddeeeeedcba"
    assert Solution().maxPower(s) == 5


def test_3():
    s = "triplepillooooow"
    assert Solution().maxPower(s) == 5


def test_4():
    s = "hooraaaaaaaaaaay"
    assert Solution().maxPower(s) == 11


def test_5():
    s = "tourist"
    assert Solution().maxPower(s) == 1
