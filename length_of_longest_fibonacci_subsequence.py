"""
LeetCode :: 873. Length of Longest Fibonacci Subsequence
jramaswami
"""


from typing import *
import functools


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        locations = {n: i for i, n in enumerate(arr)}

        @functools.cache
        def solve(a, b):
            # Looking for c.
            if a + b not in locations:
                return 0
            else:
                return 1 + solve(b, a + b)

        soln = 0
        for i, a in enumerate(arr):
            for _, b in enumerate(arr[i+1:], start=i+1):
                k = solve(a, b)
                if k > 0:
                    soln = max(soln, 2 + k)
        return soln


def test_1():
    arr = [1,2,3,4,5,6,7,8]
    expected = 5
    assert Solution().lenLongestFibSubseq(arr) == expected


def test_2():
    arr = [1,3,7,11,12,14,18]
    expected = 3
    assert Solution().lenLongestFibSubseq(arr) == expected