"""
LeetCode :: 766. Toeplitz Matrix
October 2022 Challenge
jramaswami
"""


from typing import *


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        def inbounds(r, c):
            return r >= 0 and r < len(matrix) and c >= 0 and c < len(matrix[r])

        def diagonal(r, c):
            while inbounds(r, c):
                yield r, c
                r += 1
                c += 1

        def is_toeplizt_diagonal(r, c):
            return all(matrix[r][c] == matrix[r0][c0] for r0, c0 in diagonal(r, c))

        return (
            all(is_toeplizt_diagonal(r, 0) for r, _ in enumerate(matrix))
            and
            all(is_toeplizt_diagonal(0, c) for c, _ in enumerate(matrix[0]))
        )


def test_1():
    matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    expected = True
    assert Solution().isToeplitzMatrix(matrix) == expected


def test_2():
    matrix = [[1,2],[2,2]]
    expected = False
    assert Solution().isToeplitzMatrix(matrix) == expected