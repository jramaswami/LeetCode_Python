"""
LeetCode :: December 2021 Challenge :: 221. Maximal Square
jramaswami

REF: https://www.youtube.com/watch?v=9jR5XnwtDxU
"""


class Solution:
    def maximalSquare(self, matrix):
        matrix = [[int(v) for v in row] for row in matrix]
        dp = [[0 for _ in row] for row in matrix]
        # Initialize dp.
        dp[0] = list(matrix[0])
        for r, row in enumerate(matrix):
            dp[r][0] = row[0]

        soln = 0
        for row in matrix:
            for k in row:
                if k:
                    soln = 1

        for r, row in enumerate(matrix[1:], start=1):
            for c, _ in enumerate(row[1:], start=1):
                t = min(
                    dp[r-1][c-1],
                    dp[r-1][c],
                    dp[r][c-1]
                )
                dp[r][c] = matrix[r][c] + t
                soln = max(soln, dp[r][c])

        return soln * soln


def test_1():
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    assert Solution().maximalSquare(matrix) == 4


def test_2():
    matrix = [["0","1"],["1","0"]]
    assert Solution().maximalSquare(matrix) == 1


def test_3():
    matrix = [["0"]]
    assert Solution().maximalSquare(matrix) == 0
