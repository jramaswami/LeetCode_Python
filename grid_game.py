"""
LeetCode
2017. Grid Game
January 2025 Challenge
jramaswami
"""


import itertools
from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top_row = grid[0]
        bottom_row = grid[1]
        INF = pow(10, 10)
        top_suffix = list(itertools.accumulate(top_row[::-1]))[::-1]
        bottom_prefix = list(itertools.accumulate(bottom_row))
        soln = INF
        for i, _ in enumerate(top_row):
            x = 0
            if i - 1 >= 0:
                x = max(x, bottom_prefix[i-1])
            if i + 1 < len(top_row):
                x = max(x, top_suffix[i+1])
            soln = min(x, soln)
        return soln


def test1():
    grid = [[2,5,4],[1,5,1]]
    expected = 4
    assert Solution().gridGame(grid) == expected


def test2():
    grid = [[3,3,1],[8,5,2]]
    expected = 4
    assert Solution().gridGame(grid) == expected


def test3():
    grid = [[1,3,1,15],[1,3,3,1]]
    expected = 7
    assert Solution().gridGame(grid) == expected
