"""
LeetCode
3333. Find the Original Typed String II
July 2025 Challenge
jramaswami
"""


import functools


class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = pow(10, 9) + 7

        # Group by letter
        LETTER, COUNT = 0, 1
        groups = []
        for letter in word:
            if not groups or groups[-1][LETTER] != letter:
                groups.append([letter, 1])
            else:
                groups[-1][COUNT] += 1

        @functools.cache
        def rec(g, curr_length):
            if g >= len(groups):
                if curr_length >= k:
                    return 1
                return 0

            count = groups[g][COUNT]
            result = 0
            for t in range(1, count+1):
                result += rec(g+1, curr_length + t)
                result %= MOD
            return result

        return rec(0, 0)


def test_1():
    word = "aabbccdd"
    k = 7
    expected = 5
    assert Solution().possibleStringCount(word, k) == expected


def test_2():
    word = "aabbccdd"
    k = 8
    expected = 1
    assert Solution().possibleStringCount(word, k) == expected


def test_3():
    word = "aaabbb"
    k = 3
    expected = 8
    assert Solution().possibleStringCount(word, k) == expected