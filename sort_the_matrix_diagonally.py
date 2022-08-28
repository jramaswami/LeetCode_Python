"""
LeetCode :: August 2022 Challenge :: 1329. Sort the Matrix Diagonally
jramaswami
"""


from typing import *


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        def dis_generator(r, c):
            """
            Generator returning the sequence of indices for the diagonal down
            and right starting at (r, c), where the top corner of the matrix is
            (0, 0).
            """
            while r >= 0 and r < len(mat) and c >= 0 and c < len(mat[r]):
                yield r, c
                r += 1
                c += 1

        mat1 = [[None for _ in row] for row in mat]
        for r, _ in enumerate(mat):
            t = sorted(mat[r0][c0] for r0, c0 in dis_generator(r, 0))
            for ((r1, c1), x) in zip(dis_generator(r, 0), t):
                mat1[r1][c1] = x
        for c, _ in enumerate(mat[0][1:], start=1):
            t = sorted(mat[r0][c0] for r0, c0 in dis_generator(0, c))
            for ((r1, c1), x) in zip(dis_generator(0, c), t):
                mat1[r1][c1] = x
        return mat1


def test_1():
    mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
    expected = [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
    assert Solution().diagonalSort(mat) == expected


def test_2():
    mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
    expected = [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
    assert Solution().diagonalSort(mat) == expected
