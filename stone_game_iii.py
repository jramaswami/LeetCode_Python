"""
LeetCode
1406. Stone Game III
May 2023 Challenge
jramaswami

REF: https://www.youtube.com/watch?v=HsLG5QW9CFQ
"""


import math
import functools
from typing import *


class Solution:
    def stoneGameIII(self, values: List[int]) -> str:

        @functools.cache
        def rec(i):
            if i >= len(values):
                return 0
            res = -math.inf
            for j in range(i, min(i+3, len(values))):
                res = max(res, sum(values[i:j+1]) - rec(j + 1))
            return res

        soln = rec(0)
        return "Alice" if soln > 0 else ("Bob" if soln < 0 else "Tie")


def test_1():
    values = [1,2,3,7]
    expected = 'Bob'
    assert Solution().stoneGameIII(values) == expected


def test_2():
    values = [1,2,3,-9]
    expected = 'Alice'
    assert Solution().stoneGameIII(values) == expected


def test_3():
    values = [1,2,3,6]
    expected = 'Tie'
    assert Solution().stoneGameIII(values) == expected


def test_4():
    "WA"
    values = [-2]
    expected = 'Bob'
    assert Solution().stoneGameIII(values) == expected