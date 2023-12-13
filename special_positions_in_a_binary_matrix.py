"""
LeetCode
1582. Special Positions in a Binary Matrix
December 2023 Challenge
jramaswami
"""


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_counts = [sum(row) for row in mat]
        col_counts = [sum(row[c] for row in mat) for c in range(len(mat[0]))]

        soln = 0
        for r, row in enumerate(mat):
            for c, _ in enumerate(row):
                if mat[r][c] == 1 and row_counts[r] == 1 and col_counts[c] == 1:
                    soln += 1
        return soln