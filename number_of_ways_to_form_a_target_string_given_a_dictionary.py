"""
LeetCode
1639. Number of Ways to Form a Target String Given a Dictionary
December 2024 Challenge
jramaswami
"""


import collections
import functools
from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = pow(10, 9) + 7

        # Precompute the frequency of each letter at each index
        max_length = max(len(wd) for wd in words)
        freqs = []
        for i in range(max_length):
            f = collections.Counter()
            for wd in words:
                f[wd[i]] += 1
            freqs.append(f)

        @functools.cache
        def rec(t, k):
            # Base case 1: finished target word
            if t >= len(target):
                return 1

            # Base case 2: ran out of letters
            if k >= len(freqs):
                return 0

            # Recursive case
            result = 0
            # Choose the target letter at this word index
            tl = target[t]
            result += (freqs[k][tl] * rec(t + 1, k + 1))
            # Skipt this word index
            result += rec(t, k + 1)
            return result % MOD

        return rec(0, 0)


def test_1():
    words = ["acca","bbbb","caca"]
    target = "aba"
    expected = 6
    assert Solution().numWays(words, target) == expected


def test_2():
    words = ["abba","baab"]
    target = "bab"
    expected = 4
    assert Solution().numWays(words, target) == expected
