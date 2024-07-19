"""
LeetCode
1380. Lucky Numbers in a Matrix
July 2024 Challenge
jramaswami
"""


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        INF = pow(10,10)
        row_mins = [INF for _ in matrix]
        col_maxes = [-INF for _ in matrix[0]]
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                row_mins[r] = min(row_mins[r], val)
                col_maxes[c] = max(col_maxes[c], val)

        soln = []
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if row_mins[r] == val and col_maxes[c] == val:
                    soln.append(val)
        return soln