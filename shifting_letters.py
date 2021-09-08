"""
LeetCode :: September 2021 Challenge :: Shifting Letters
jramaswami
"""


class Solution:
    def shiftingLetters(self, S, shifts):

        def encode(c):
            """Transform character into [0, 26)."""
            return ord(c) - ord('a')

        def decode(n):
            """Transform [0, 26) into a character."""
            return chr((n % 26) + ord('a'))

        # Use suffix sum to determine the total number of shifts for each letter.
        shifts[0] %= 26
        for i in range(len(shifts)-2, -1, -1):
            shifts[i] = shifts[i] + shifts[i+1] % 26

        return "".join(decode(encode(c) + shift) for c, shift in zip(S, shifts))


def test_1():
    S = "abc"
    shifts = [3,5,9]
    assert Solution().shiftingLetters(S, shifts) == "rpl"


def test_2():
    S = "aaa"
    shifts = [1,2,3]
    assert Solution().shiftingLetters(S, shifts) == "gfd"
