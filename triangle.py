"""
Leet Code :: April 2021 Challenge :: Triangle
jramaswami
"""
from typing import *
from math import inf

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[inf for _ in row] for row in triangle]
        dp[0][0] = triangle[0][0]
        for r, row in enumerate(triangle[:-1]):
            for c, val in enumerate(row):
                dp[r+1][c] = min(triangle[r+1][c] + dp[r][c], dp[r+1][c])
                dp[r+1][c+1] = min(triangle[r+1][c+1] + dp[r][c], dp[r+1][c+1])
        return min(dp[-1])


def test_1():
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    assert Solution().minimumTotal(triangle) == 11

def test_3():
    triangle = [[-10]]
    assert Solution().minimumTotal(triangle) == -10