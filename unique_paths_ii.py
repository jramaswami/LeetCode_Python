"""
Leet Code :: April 2021 Challenge :: Unique Paths II
jramaswami
"""
from typing import *


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0 for _ in row] for row in  obstacleGrid]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        for r, row in enumerate(obstacleGrid):
            for c, _ in enumerate(row):
                if obstacleGrid[r][c]:
                    continue
                if r > 0:
                    dp[r][c] += dp[r-1][c]
                if c > 0:
                    dp[r][c] += dp[r][c-1]
        return dp[-1][-1]


def test_1():
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    assert Solution().uniquePathsWithObstacles(obstacleGrid) == 2


def test_2():
    obstacleGrid = [[0,1],[0,0]]
    assert Solution().uniquePathsWithObstacles(obstacleGrid) == 1


def test_3():
    obstacleGrid = [[1]]
    assert Solution().uniquePathsWithObstacles(obstacleGrid) == 0