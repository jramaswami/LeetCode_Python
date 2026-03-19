"""
LeetCode
3212. Count Submatrices With Equal Frequency of X and Y
March 2026 Challenge
jramaswami
"""


from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        dp = {}
        for key in 'XY.':
            dp[key] = [[0 for _ in row] for row in grid]
        soln = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                for key in 'XY.':
                    if r - 1 >= 0:
                        dp[key][r][c] += dp[key][r-1][c]
                    if c - 1 >= 0:
                        dp[key][r][c] += dp[key][r][c-1]
                    if r - 1 >= 0 and c - 1 >= 0:
                        dp[key][r][c] -= dp[key][r-1][c-1]
                dp[val][r][c] += 1
                if dp['X'][r][c] and dp['X'][r][c] == dp['Y'][r][c]:
                    soln += 1
        return soln