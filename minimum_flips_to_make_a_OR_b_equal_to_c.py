"""
LeetCode
1318. Minimum Flips to Make a OR b Equal to c
June 2023 Challenge
jramaswami
"""


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        soln = 0
        for _ in range(32):
            if c & 1:
                # bit should be set
                if a & 1 == 0 and b & 1 == 0:
                    soln += 1
            else:
                # bit should not be set
                if a & 1:
                    soln += 1
                if b & 1:
                    soln += 1

            a = a >> 1
            b = b >> 1
            c = c >> 1

        return soln


def test_1():
    a = 2
    b = 6
    c = 5
    expected = 3
    assert Solution().minFlips(a, b, c) == expected


def test_2():
    a = 4
    b = 2
    c = 7
    expected = 1
    assert Solution().minFlips(a, b, c) == expected


def test_3():
    a = 1
    b = 2
    c = 3
    expected = 0
    assert Solution().minFlips(a, b, c) == expected