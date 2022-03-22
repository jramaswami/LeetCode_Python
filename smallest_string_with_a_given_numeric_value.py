"""
LeetCode :: March 2022 Challenge :: 1663. Smallest String With A Given Numeric Value
jramaswami
"""


class Solution:
    def getSmallestString(self, n, k):
        soln = ['a' for _ in range(n)]
        j = n
        for i, _ in enumerate(soln):
            delta = min(25, k - j)
            soln[i] = chr(ord('a') + delta)
            j += delta
        return "".join(reversed(soln))


def test_1():
    n = 3
    k = 27
    expected = "aay"
    assert Solution().getSmallestString(n, k) == expected


def test_2():
    n = 5
    k = 73
    expected = "aaszz"
    assert Solution().getSmallestString(n, k) == expected


def test_3():
    n = 3
    k = 3
    expected = "aaa"
    assert Solution().getSmallestString(n, k) == expected
