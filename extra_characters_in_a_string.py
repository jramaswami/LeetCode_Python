"""
LeetCode
2707. Extra Characters in a String
September 2023 Challenge
jramaswami
"""


import functools
from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        @functools.cache
        def score(left, right):
            if s[left:right] in dictionary:
                return 0
            return right - left

        @functools.cache
        def rec(left, right):
            # Base case, end of string
            if right >= len(s):
                return score(left, right)

            return min(
                # You can split s[left:right] off
                score(left, right) + rec(right, right+1),
                # You can continue building the word
                rec(left, right+1)
            )

        return rec(0, 0)



def test_1():
    s = "leetscode"
    dictionary = ["leet","code","leetcode"]
    expected = 1
    assert Solution().minExtraChar(s, dictionary) == expected


def test_2():
    s = "sayhelloworld"
    dictionary = ["hello","world"]
    expected = 3
    assert Solution().minExtraChar(s, dictionary) == expected