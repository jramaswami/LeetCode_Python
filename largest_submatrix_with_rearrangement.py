"""
LeetCode
1727. Largest Submatrix With Rearrangements
November 2023 Challenge
jramaswami
"""


from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        depth = [[0 for _ in row] for row in matrix]
        depth[0] = list(matrix[0])
        for r, matrix_row in enumerate(matrix[1:], start=1):
            for c, matrix_value in enumerate(matrix_row):
                if matrix_value == 1:
                    depth[r][c] = depth[r-1][c] + 1
                else:
                    depth[r][c] = 0

        soln = 0
        for row in depth:
            row.sort(reverse=True)
            result = max((i+1) * d for i, d in enumerate(row))
            soln = max(soln, result)
        return soln


def test_1():
    matrix = [[0,0,1],[1,1,1],[1,0,1]]
    expected = 4
    assert Solution().largestSubmatrix(matrix) == expected


def test_2():
    matrix = [[1,0,1,0,1]]
    expected = 3
    assert Solution().largestSubmatrix(matrix) == expected


def test_3():
    matrix = [[1,1,0],[1,0,1]]
    expected = 2
    assert Solution().largestSubmatrix(matrix) == expected