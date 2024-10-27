"""
LeetCode
1277. Count Square Submatrices with All Ones
October 2024 Challenge
jramaswami

Thank You Larry!
"""


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        soln = 0
        dp = [[ 0 for _ in row] for row in matrix]
        for r, row in enumerate(matrix):
            for c, _ in enumerate(row):
                if matrix[r][c] == 1:
                    dp[r][c] = 1
                    if r - 1 >= 0 and c - 1 >= 0:
                        dp[r][c] = min(dp[r-1][c], dp[r-1][c-1], dp[r][c-1]) + 1
                    soln += dp[r][c]
        return soln
