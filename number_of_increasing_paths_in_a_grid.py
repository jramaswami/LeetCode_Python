"""
LeetCode
2328. Number of Increasing Paths in a Grid
June 2023 Challenge
jramaswami
"""


import collections
import operator
from typing import *


Cell = collections.namedtuple('Cell', ['value', 'row', 'col'])


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        # Sort the grid cells by value
        # O(log(m*n))
        # Process cells in order with caching the number of ways to a cell
        # O(m*n)
        # Initially a cell has 1 way.
        MOD = pow(10, 9)
        soln = 0
        dp = [[1 for _ in row] for row in grid]

        def inbounds(r, c):
            return (
                r >= 0 and c >= 0 and
                r < len(grid) and c < len(grid[r])
            )


        OFFSETS = ((0, 1), (0, -1), (1, 0), (-1, 0))
        def increasing_neighbors(r, c):
            for dc, dr in OFFSETS:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0) and grid[r0][c0] > grid[r][c]:
                    yield r0, c0

        cells = [Cell(grid[r][c], r, c) 
                    for r, _ in enumerate(grid) 
                    for c, _ in enumerate(grid[r])
        ]
        cells.sort(key=operator.attrgetter('value'))

        for _, r, c in cells:
            soln = (soln + dp[r][c]) % MOD
            for r0, c0 in increasing_neighbors(r, c):
                dp[r0][c0] = (dp[r0][c0] + dp[r][c]) % MOD
        return soln


def test_1():
    grid = [[1,1],[3,4]]
    expected = 8
    assert Solution().countPaths(grid) == expected


def test_2():
    grid = [[1],[2]]
    expected = 3
    assert Solution().countPaths(grid) == expected
