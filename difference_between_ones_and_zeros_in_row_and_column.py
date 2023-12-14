"""
LeetCode
2482. Difference Between Ones and Zeros in Row and Column
December 2023 Challenge
jramaswami
"""


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row_ones = [sum(row) for row in grid]
        col_ones = [sum(row[c] for row in grid) for c, _ in enumerate(grid[0])]
        N = len(grid)
        row_zeros = [N - r for r in row_ones]
        M = len(grid[0])
        col_zeros = [M - c for c in col_ones]

        diff = [[0 for _ in row] for row in grid]
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                diff[i][j] = row_ones[i] + col_ones[j] - row_zeros[i] - col_zeros[j]
        return diff