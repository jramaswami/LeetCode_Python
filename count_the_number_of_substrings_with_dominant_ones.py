"""
LeetCode
3234. Count the Number of Substrings With Dominant Ones
November 2025 Challenge
jramaswami
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        soln = 0
        for i, _ in enumerate(s):
            curr_ones = 0
            for j, val in enumerate(s[i:], start=i):
                if val == '1':
                    curr_ones += 1
                curr_zeros = (j - i + 1) - curr_ones
                if curr_ones >= pow(curr_zeros, 2):
                    soln += 1
        return soln


def test_1():
    s = "00011"
    assert Solution().numberOfSubstrings(s) == 5


def test_2():
    s = "101101"
    assert Solution().numberOfSubstrings(s) == 16