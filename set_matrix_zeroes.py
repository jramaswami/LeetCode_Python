"""
LeetCode :: August 2021 Challenge :: Set Matrix Zeroes
jramaswami
"""


class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in place.
        """
        if matrix == []:
            return

        zero_row = [False for _ in matrix]
        zero_col = [False for _ in matrix[0]]

        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if val == 0:
                    zero_row[r] = True
                    zero_col[c] = True

        for r, row in enumerate(matrix):
            for c, _ in enumerate(row):
                if zero_row[r] or zero_col[c]:
                    matrix[r][c] = 0


def test_1():
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    expected = [[1,0,1],[0,0,0],[1,0,1]]
    Solution().setZeros(matrix)
    assert matrix == expected


def test_2():
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    expected = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    Solution().setZeros(matrix)
    assert matrix == expected


def test_3():
    matrix = []
    expected = []
    Solution().setZeros(matrix)
    assert matrix == expected
