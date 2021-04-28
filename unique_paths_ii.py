"""
Leet Code :: April 2021 Challenge :: Unique Paths II
jramaswami
"""
from typing import *
from math import factorial


def nCk(n, k):
    """Return binomial coefficient for n choose k."""
    return factorial(n) // (factorial(k) * factorial(n - k))


def find_obstacle(obstacleGrid):
    """Return coordinates of obstacle."""
    for r, row in enumerate(obstacleGrid):
        for c, val in enumerate(row):
            if val == 1:
                return (r, c)
    return None, None


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Find the number of paths from the start to the end.
        H = len(obstacleGrid)
        W = len(obstacleGrid[0])
        n = H + W - 2
        k = W - 1
        soln = nCk(n, k)

        # Find the obstacle
        obstacle_r, obstacle_c = find_obstacle(obstacleGrid)

        # If there is an obstacle find the number of paths that go through
        # the cell occupied by the obstacle.
        if obstacle_r is not None:
            # Find the number of paths to the cell occupied by obstacle.
            H0 = obstacle_r + 1
            W0 = obstacle_c + 1
            n = H0 + W0 - 2
            k = W0 - 1
            d_to = nCk(n, k)

            # Find the number of paths from the cell occupied by obstacle.
            H0 = H - obstacle_r
            W0 = W - obstacle_c
            n = H0 + W0 - 2
            k = W0 - 1
            d_from = nCk(n, k)

            # Compute the number of paths through the obstacle.
            d = d_to * d_from

            # Subtract those paths from the total paths.
            soln -= d

        return soln


def test_1():
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    assert Solution().uniquePathsWithObstacles(obstacleGrid) == 2


def test_2():
    obstacleGrid = [[0,1],[0,0]]
    assert Solution().uniquePathsWithObstacles(obstacleGrid) == 1


def test_3():
    obstacleGrid = [[1]]
    assert Solution().uniquePathsWithObstacles(obstacleGrid) == 0