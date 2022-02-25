"""
LeetCode :: February 2022 Challenge :: 165. Compare Version Numbers
jramaswami
"""


import itertools


class Solution:

    def compareVersion(self, version1, version2):
        v1 = [int(s) for s in version1.split('.')]
        v2 = [int(s) for s in version2.split('.')]
        for a, b in itertools.zip_longest(v1, v2, fillvalue=0):
            if a < b:
                return -1
            if a > b:
                return 1
        return 0


def test_1():
    version1 = "1.01"
    version2 = "1.001"
    expected = 0
    assert Solution().compareVersion(version1, version2) == expected


def test_2():
    version1 = "1.0"
    version2 = "1.0.0"
    expected = 0
    assert Solution().compareVersion(version1, version2) == expected


def test_3():
    version1 = "0.1"
    version2 = "1.1"
    expected = -1
    assert Solution().compareVersion(version1, version2) == expected


def test_4():
    version1 = "7.44.1.1"
    version2 = "7.044.0.1"
    expected = 1
    assert Solution().compareVersion(version1, version2) == expected
