"""
LeetCode
1504. Count Submatrices With All Ones
August 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        # Compute a prefix sum for the matrix
        # S[row][column] = sum for submatrix that is
        # mat[0][0] to mat[row][column] (inclusive)
        S = [[0 for _ in row] for row in mat]
        for r, row in enumerate(mat):
            row_sum = 0
            for c, val in enumerate(row):
                row_sum += val
                if r == 0:
                    S[r][c] = row_sum
                else:
                    S[r][c] = row_sum + S[r-1][c]

        def get(r, c):
            """Function retrieve value from prefix sum.
            Returns zero if cell is out of bounds."""
            if 0 <= r < len(S) and 0 <= c < len(S[r]):
                return S[r][c]
            return 0

        def get_submat_sum(r0, c0, r1, c1):
            """Function to return the sum of values in
            the submatrix."""
            T = get(r1, c1)
            A = get(r0-1, c0-1)
            B = get(r0-1, c1)
            C = get(r1, c0-1)
            return T - B - C + A
        
        # Iterate over all submatrices. If the sum of the
        # values in the submatrix is equal to the area of
        # the submatrix, then it is all ones.
        soln = 0
        N = len(mat)
        M = len(mat[0])
        for r0 in range(N):
            for r1 in range(r0, N):
                for c0 in range(M):
                    for c1 in range(c0, M):
                        submat_area = (r1 - r0 + 1) * (c1 - c0 + 1)
                        submat_sum = get_submat_sum(r0, c0, r1, c1)
                        if submat_sum == submat_area:
                            soln += 1
        return soln


def test_1():
    mat = [[1,0,1],[1,1,0],[1,1,0]]
    expected = 13
    assert Solution().numSubmat(mat) == expected


def test_2():
    mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
    expected = 24
    assert Solution().numSubmat(mat) == expected
