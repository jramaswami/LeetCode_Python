"""
LeetCode
931. Minimum Falling Path Sum
December 2022 Challenge
jramaswami
"""


from typing import *
import math


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [[math.inf for _ in row] for row in matrix]
        dp[0] = list(matrix[0])
        for r, row in enumerate(matrix[:-1]):
            for c, _ in enumerate(row):
                for dc in (-1, 0, 1):
                    c0 = c + dc
                    if c0 >= 0 and c0 < len(row):
                        dp[r+1][c0] = min(dp[r+1][c0], matrix[r+1][c0] + dp[r][c])
        return min(dp[-1])


def test_1():
    matrix = [[2,1,3],[6,5,4],[7,8,9]]
    expected = 13
    assert Solution().minFallingPathSum(matrix) == expected


def test_2():
    matrix = matrix = [[-19,57],[-40,-5]]
    expected = -59
    assert Solution().minFallingPathSum(matrix) == expected
