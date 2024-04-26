"""
LeetCode
1289. Minimum Falling Path Sum II
April 2024 Challenge
jramaswami
"""


from typing import List
import math


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        dp = [[math.inf for _ in row] for row in grid]
        dp[0] = grid[0]
        for r, row in enumerate(grid[:-1]):
            for c, _ in enumerate(row):
                for i, x in enumerate(dp[r]):
                    if c == i:
                        # Do not choose from same column
                        continue
                    dp[r+1][c] = min(dp[r+1][c], grid[r+1][c] + x)
        return min(dp[-1])


def test_1():
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    expected = 13
    result = Solution().minFallingPathSum(grid)
    assert result == expected


def test_2():
    grid = [[7]]
    expected = 7
    result = Solution().minFallingPathSum(grid)
    assert result == expected


def test_3():
    "WA"
    grid = [[-73,61,43,-48,-36],[3,30,27,57,10],[96,-76,84,59,-15],[5,-49,76,31,-7],[97,91,61,-46,67]]
    expected = -192
    result = Solution().minFallingPathSum(grid)
    assert result == expected