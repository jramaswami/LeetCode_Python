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
        h = [(c, i) for i, c in enumerate(s)]
        p = []
        heapq.heapify(h)
        j = 0  # Points to next unused character
        while h:
            while t and t[-1] < h[0][0]:
                p.append(t[-1])
                t.pop()
            c, i = heapq.heappop(h)
            if j <= i:
                for x in range(j, i):
                    t.append(s[x])
                p.append(c)
                j = i + 1
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