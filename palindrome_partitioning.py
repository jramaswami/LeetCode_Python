"""
LeetCode
131. Palindrome Partitioning
January 2023
jramaswami
"""


from typing import *
import functools


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        soln = []

        @functools.cache
        def is_palindrome(left, right):
            if right < left:
                return True
            return s[left] == s[right] and is_palindrome(left+1, right-1)

        def rec(i, acc):
            if i >= len(s):
                soln.append(list(acc))

            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    acc.append(s[i:j+1])
                    rec(j+1, acc)
                    acc.pop()

        rec(0, [])
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