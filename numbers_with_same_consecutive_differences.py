"""
LeetCode :: September 2022 Challenge :: 967. Numbers With Same Consecutive Differences
jramaswami
"""


from typing import *


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        def rec(x, i, acc):
            if i == n:
                acc.append(x)
                return

            if i == 0:
                for y in range(1, 10):
                    rec(y, 1, acc)
            else:
                z = x % 10
                for y in range(10):
                    if abs(z - y) == k:
                        rec((x * 10) + y, i + 1, acc)

        acc = []
        rec(0, 0, acc)
        return acc


def test_1():
    n = 3
    k = 7
    expected = [181,292,707,818,929]
    result = Solution().numsSameConsecDiff(n, k)
    assert sorted(expected) == sorted(result)


def test_2():
    n = 2
    k = 1
    expected = [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
    result = Solution().numsSameConsecDiff(n, k)
    assert sorted(expected) == sorted(result)