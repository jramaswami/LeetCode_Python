"""
Leet Code :: June 2022 Challenge :: Range Sum Query 2D - Immutable
jramaswami
"""


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = [[0 for _ in row] for row in matrix]
        for r, row in enumerate(matrix):
            for c, _ in enumerate(row):
                self.prefix[r][c] = (
                    self.matrix[r][c] +
                    self._get_prefix(r-1, c) +
                    self._get_prefix(r, c-1) -
                    self._get_prefix(r-1, c-1)
                )

    def _get_prefix(self, r, c):
        if r < 0 or c < 0:
            return 0
        return self.prefix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self._get_prefix(row2, col2) -
            self._get_prefix(row1-1, col2) -
            self._get_prefix(row2, col1-1) +
            self._get_prefix(row1-1, col1-1)
        )

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
