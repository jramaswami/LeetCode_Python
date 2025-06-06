"""
LeetCode
2434. Using a Robot to Print the Lexicographically Smallest String
June 2025 Challenge
jramaswami
"""


import itertools
import heapq


class Solution:
    def robotWithString(self, s: str) -> str:
        t = []
        p = []

        # Determine the index and letter that is the minimum from a given
        # position to the end of the string.
        h = []
        curr = (s[-1], len(s)-1)
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            curr = min(curr, (c, i))
            h.append(curr)
        h = h[::-1]

        i = 0
        while i < len(s):
            target_letter, target_index = h[i]
            # While the last character in t is less than or equal to the
            # minimum character in s from i to the end, put the character
            # from t in p
            while t and t[-1] <= target_letter:
                p.append(t.pop())

            # Go to minimum character from i to the end of the string, putting
            # the letters on t
            while i <= target_index:
                t.append(s[i])
                i += 1

        return "".join(itertools.chain(p, reversed(t)))


def test_1():
    s = "zza"
    expected = "azz"
    assert Solution().robotWithString(s) == expected


def test_2():
    s = "bac"
    expected = "abc"
    assert Solution().robotWithString(s) == expected


def test_3():
    s = "bdda"
    expected = "addb"
    assert Solution().robotWithString(s) == expected


def test_4():
    "WA"
    s = "vzhofnpo"
    expected = "fnohopzv"
    assert Solution().robotWithString(s) == expected