"""
LeetCode :: January 2022 Challenge :: 131. Palindrome Partitioning
jramaswami
"""


from functools import cache
from typing import *


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        @cache
        def is_palindrome(left: int, right: int):
            "Returns True if s[left:right+1] is a palindrome."
            if left >= right:
                return True

            if s[left] == s[right]:
                return is_palindrome(left + 1, right - 1)

            return False

        def solve(left, acc, soln):
            "DFS to indentify all possible partitions."
            if left >= len(s):
                soln.append(list(acc))

            for right in range(left, len(s)):
                if is_palindrome(left, right):
                    acc.append(s[left:right+1])
                    solve(right+1, acc, soln)
                    acc.pop()

        acc = []
        soln = []
        solve(0, acc, soln)
        return soln


def test_1():
    s = "aab"
    expected = [["a","a","b"],["aa","b"]]
    result = Solution().partition(s)
    assert sorted(result) == sorted(expected)


def test_2():
    s = "a"
    expected = [["a"]]
    result = Solution().partition(s)
    assert sorted(result) == sorted(expected)


def test_3():
    s = "a" * 16
    expected = [["a"]]
    result = Solution().partition(s)
    assert sorted(result) == sorted(expected)
