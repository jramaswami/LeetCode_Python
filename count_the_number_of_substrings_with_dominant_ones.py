"""
LeetCode
3234. Count the Number of Substrings With Dominant Ones
November 2025 Challenge
jramaswami
"""


import itertools


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ones_prefix = list(itertools.accumulate(int(x) for x in s))

        def get(left, right):
            if left == 0:
                return ones_prefix[right]
            return ones_prefix[right] - ones_prefix[left - 1]

        soln = 0
        for i, _ in enumerate(s):
            j = i
            while j < len(s):
                curr_ones = get(i, j)
                curr_zeros = (j - i + 1) - curr_ones
                if curr_ones >= pow(curr_zeros, 2):
                    soln += 1
                    j += 1
                elif curr_zeros:
                    j = max(j + 1, i + pow(curr_zeros, 2))
        return soln


def test_1():
    s = "00011"
    assert Solution().numberOfSubstrings(s) == 5


def test_2():
    s = "101101"
    assert Solution().numberOfSubstrings(s) == 16