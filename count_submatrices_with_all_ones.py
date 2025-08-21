"""
LeetCode
1504. Count Submatrices With All Ones
August 2025 Challenge
jramaswami
"""


import math
from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        # S[row][column] = the number of ones to the left of S[row][column]
        S = [[0 for _ in row] for row in mat]
        for r, row in enumerate(mat):
            curr_ones = 0
            for c, val in enumerate(row):
                if val == 0:
                    curr_ones = 0
                else:
                    curr_ones += 1
                S[r][c] = curr_ones

        # Iterate over the possible top right and bottom
        # right corners for all submatrices
        soln = 0
        N = len(mat)
        M = len(mat[0])
        for c in range(M):
            for start_row in range(N):
                min_width = math.inf
                for end_row in range(start_row, N):
                    # Add the current row to the minimum width
                    min_width = min(min_width, S[end_row][c])
                    # The widest matrix with to right corner
                    # (start_row, c) and bottom right corner
                    # (end_row, c) is the minimum width.
                    soln += min_width
        return soln


def test_1():
    mat = [[1,0,1],[1,1,0],[1,1,0]]
    expected = 13
    assert Solution().numSubmat(mat) == expected


def test_2():
    mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
    expected = 24
    assert Solution().numSubmat(mat) == expected
