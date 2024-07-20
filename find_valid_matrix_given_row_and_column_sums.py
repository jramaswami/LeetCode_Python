"""
LeetCode
1605. Find Valid Matrix Given Row and Column Sums
July 2024 Challenge
jramaswami
"""


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        soln = [[0 for _ in colSum] for _ in rowSum]
        actual_row_sums = [0 for _ in rowSum]
        actual_row_sums[0] = sum(colSum)
        soln[0] = colSum
        for r, row in enumerate(soln[:-1]):
            for c, x in enumerate(row):
                d = actual_row_sums[r] - rowSum[r]
                if d == 0:
                    break
                # Invariant d > 0
                if x < d:
                    # Move all of x to next row.
                    soln[r+1][c] = x
                    soln[r][c] = 0
                    # Update the row_sums for this row and the next.
                    actual_row_sums[r] -= x
                    actual_row_sums[r+1] += x
                else:
                    # Move part of x to next row.
                    soln[r+1][c] = d
                    soln[r][c] = x - d
                    # Update the row_sums for this row and the next.
                    actual_row_sums[r] -= d
                    actual_row_sums[r+1] += d
        return soln