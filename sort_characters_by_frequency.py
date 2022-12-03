"""
LeetCode
451. Sort Characters By Frequency
December 2022 Challenge
jramaswami
"""


import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        ctr = collections.Counter(s)
        return "".join(c * f for c, f in sorted(ctr.items(), key=lambda t: (-t[1], t[0])))



def test_1():
    s = "tree"
    expected = "eert"
    assert Solution().frequencySort(s) == expected


def test_2():
    s = "cccaaa"
    expected = "aaaccc"
    assert Solution().frequencySort(s) == expected


def test_3():
    s = "Aabb"
    expected = "bbAa"
    assert Solution().frequencySort(s) == expected