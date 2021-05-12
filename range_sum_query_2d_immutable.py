"""
Leet Code :: May 2021 Challenge :: Range Sum Query 2D - Immutable
jramaswami
"""
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        soln = 0
        for row in self.matrix[row1:row2+1]:
            soln += sum(row[col1:col2+1])
        return soln       


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
