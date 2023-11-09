"""
LeetCode
1759. Count Number of Homogenous Substrings
November 2023 Challenge
jramaswami
"""


class Solution:
    def countHomogenous(self, s: str) -> int:
        curr_letter = s[0]
        curr_length = 1
        soln = 1
        for c in s[1:]:
            if c == curr_letter:
                curr_length += 1
            else:
                curr_length = 1
                curr_letter = c
            soln += curr_length
        return soln


def test_1():
    s = "abbcccaa"
    expected = 13
    assert Solution().countHomogenous(s) == expected


def test_2():
    s = "xy"
    expected = 2
    assert Solution().countHomogenous(s) == expected


def test_3():
    s = "zzzzz"
    expected = 15
    assert Solution().countHomogenous(s) == expected