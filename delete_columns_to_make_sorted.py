"""
LeetCode
944. Delete Columns to Make Sorted
January 2023 Challenge
jramaswami
"""


import itertools
from typing import *


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        def column_generator(c):
            "Generator for values in column c of strs."
            for row in strs:
                yield row[c]

        def column_is_sorted(c):
            "Return True if column c of strs is sorted."
            return all(a <= b for a, b in zip(
                column_generator(c),
                itertools.islice(column_generator(c), 1, None)))

        return sum(0 if column_is_sorted(c) else 1 for c, _ in enumerate(strs[0]))


def test_1():
    strs = ["cba","daf","ghi"]
    expected = 1
    assert Solution().minDeletionSize(strs) == expected


def test_2():
    strs = ["a","b"]
    expected = 0
    assert Solution().minDeletionSize(strs) == expected


def test_3():
    strs = ["zyx","wvu","tsr"]
    expected = 3
    assert Solution().minDeletionSize(strs) == expected
