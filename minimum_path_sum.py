"""
LeetCode
64. Minimum Path Sum
March 2023 Challenge
jramaswami
"""


import math
from typing import *


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[math.inf for _ in row] for row in grid]
        dp[0][0] = grid[0][0]

        def get(r, c):
            if r < 0 or c < 0:
                return math.inf
            return dp[r][c]

        for r, row in enumerate(grid):
            for c, _ in enumerate(row):
                dp[r][c] = min(
                    dp[r][c],
                    grid[r][c] + get(r-1, c),
                    grid[r][c] + get(r, c-1)
                )
        return dp[-1][-1]


def test_1():
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    expected = 7
    assert Solution().minPathSum(grid) == expected


def test_2():
    grid = [[1,2,3],[4,5,6]]
    expected = 12
    assert Solution().minPathSum(grid) == expected