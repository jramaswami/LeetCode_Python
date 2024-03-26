"""
LeetCode
60. Permutation Sequence
jramaswami
"""


import math
from typing import List


class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        def rec(digits: List[int], t: int) -> str:
            if len(digits) == 1:
                return digits[0]

            x = math.factorial(len(digits) - 1)
            i = 0
            while t + x <= k:
                i += 1
                t += x
            return digits[i] + rec([d for d in digits if d != digits[i]], t)

        return rec(list(str(d) for d in range(1, n+1)), 1)


def test_1():
    n = 3
    k = 3
    expected = '213'
    assert Solution().getPermutation(n, k) == expected


def test_2():
    n = 4
    k = 9
    expected = '2314'
    assert Solution().getPermutation(n, k) == expected


def test_3():
    n = 3
    k = 1
    expected = "123"