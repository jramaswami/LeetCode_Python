"""
LeetCode :: April 2021 Challenge :: Number of Submatrices That Sum to Target
jramaswami
"""
from typing import *

 
def get_sum(top_r, top_c, bot_r, bot_c, sums):
    """Return the sum of the submatrix (top_r, top_c) to (bot_r, bot_c)"""
    A = sums[bot_r][bot_c]                                            # Whole box
    B = sums[top_r - 1][bot_c] if top_r > 0 else 0                    # Top
    C = sums[bot_r][top_c - 1] if top_c > 0 else 0                    # Left
    D = sums[top_r - 1][top_c - 1] if top_r > 0 and top_c > 0 else 0  # Overlap of top / left
    return A - B - C + D


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        sums = [[0 for _ in row] for row in matrix]
        for r, row in enumerate(matrix):
            col_sum = 0
            for c, _ in enumerate(row):
                col_sum += matrix[r][c]
                prev_row_sum = sums[r-1][c] if r > 0 else 0
                sums[r][c] = col_sum + prev_row_sum

        soln = 0
        for top_r, top_row in enumerate(matrix):
            for top_c, _ in enumerate(top_row):
                for bot_r, bot_row in enumerate(matrix[top_r:], start=top_r):
                    for bot_c, _ in enumerate(bot_row[top_c:], start=top_c):
                        S = get_sum(top_r, top_c, bot_r, bot_c, sums)
                        if S == target:
                            soln += 1

        return soln



def test_1():
    matrix = [[0,1,0],[1,1,1],[0,1,0]]
    target = 0
    assert Solution().numSubmatrixSumTarget(matrix, target) == 4

def test_2():
    matrix = [[1,-1],[-1,1]]
    target = 0
    assert Solution().numSubmatrixSumTarget(matrix, target) == 5

def test_3():
    matrix = [[904]]
    target = 0
    assert Solution().numSubmatrixSumTarget(matrix, target) == 0

def test_4():
    """TLE"""
    matrix = [[1,0,0,1,0,0,1,1,1,1,1,1,1,0,1,0,0,1,0,0,1,1,1,1,1,1,0,1,0,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0,0,0,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,1,0,1,1,1,0,1,1,0],[0,0,0,0,1,0,1,0,1,1,1,1,1,0,1,1,0,1,1,0,0,1,1,0,0,1,0,1,0,0,1,0,0,0,0,0,1,0,1,1,1,1,1,0,1,1,0,1,0,0,1,1,0,0,1,1,0,0,0,0,0,1,0,0,0,1,0,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,0,0,0,1,0,1,1,1,0,0,0,0,0,1,1],[0,1,0,0,1,0,0,0,0,1,1,1,1,0,1,1,0,0,1,0,1,1,0,1,0,0,0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,0,1,0,1,1,1,0,0,0,1,1,1,1,0,1,0,1,1,0,1,0,0,1,1,0,0,1,1,0,0,1,0,0,0,1,1,0,1,0,0,1,1,0,0,1,0,1,1,0,1,0,0,1,1],[1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,1,0,0,1,1,0,0,0,0,0,1,0,1,1,0,0,1,1,1,0,0,1,0,0,1,0,0,0,1,1,1,0,0,1,0,1,0,1,0,0,1,1,0,1,1,0,0,0,0,1,1,1,1,1,0,1,0,1,1,0,1,1,1,0,1,1,0,1,0,1,0,0,0,0,1,0,1,0,0,1],[1,0,0,1,1,1,0,0,0,1,1,1,1,0,1,0,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,1,0,1,0,1,1,1,1,0,0,0,1,1,0,1,1,1,0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,0,0,0,0,1,1,0,0,1,1,1,0,1,1,0,1,0,0,0,1,1,0,0,0,1,1,1,1,0,0,1],[1,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,1,1,0,1,1,0,1,0,0,1,0,0,0,0,0,0,1,1,1,0,0,0,1,0,0,1,1,1,1,1,1,1,0,1,1,0,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,1,1,0,1,1,0,1,0,0,1,1,1,1],[1,0,0,0,0,1,0,0,0,0,1,0,1,1,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,0,1,0,1,0,1,0,0,1,1,0,1,0,1,1,1,1,0,0,1,0,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,1,0,0,0,0,0,1,0,1,0,1,0],[1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,1,0,0,0,1,1,1,1,0,0,1,1,1,0,0,0,1,1,1,1,0,0,1,0,0,0,1,1,0,0,0,1,1,1,1,1,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0],[1,0,0,0,0,0,0,1,0,1,1,0,1,1,1,1,0,1,1,0,0,0,0,1,1,0,1,0,0,1,0,0,1,0,1,1,0,1,0,0,0,1,1,0,1,1,1,1,0,1,0,0,1,0,0,1,0,1,1,0,1,1,0,1,0,1,0,1,1,0,0,0,1,1,1,0,1,0,1,1,1,1,0,1,0,0,0,0,1,1,0,1,1,1,0,0,1,1,0,0],[1,0,0,0,1,1,1,1,1,0,1,0,1,0,0,1,1,0,0,0,1,0,0,0,1,0,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,0,1,1,0,0,1,1,1,0,0,1,0,0,1,1,1,0,0,0,0,0,0,0,1,0,0],[0,1,0,1,0,1,0,0,1,0,1,1,0,1,1,0,1,1,0,0,1,0,0,1,0,1,1,1,1,0,1,1,0,0,0,0,1,0,1,0,1,0,0,0,1,1,1,1,0,0,1,0,1,0,1,0,1,0,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0,1,0,0,1,1,0,1,1,0,0,1,1,0,1,1,1,0,0,0,1,1,0],[0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,1,1,1,0,0,1,0,0,0,0,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,0,0,1,0,1,0,1,1,1,0,1,0,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0,0,1,1,1,1,0,0,0,0,0,1,1,0,1,0,1,1,1,1,0,1,0,0,0,1,1,1],[0,0,0,0,1,1,1,0,0,1,1,1,0,0,1,0,0,1,0,0,0,0,1,1,1,0,1,1,0,0,0,0,0,0,0,1,1,0,1,1,1,1,0,1,0,1,0,0,0,1,1,1,0,1,0,1,1,0,0,0,0,0,0,1,0,0,1,1,0,1,0,1,1,0,0,0,0,0,0,1,0,0,0,0,1,0,1,1,0,0,1,0,1,1,0,1,0,0,1,0],[1,0,0,0,0,0,1,1,0,0,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,0,1,1,0,1,1,0,1,0,0,0,0,0,1,1,1,1,1,1,0,1,0,0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,1,1,1,1,1,1,1,0,1,0,1,1,0,1,0,0,1,1,1,0,0,0,1,0,0,1,1,0,0,0],[0,0,0,1,1,1,0,1,1,0,1,0,1,1,0,0,1,1,0,1,1,0,0,1,1,0,1,1,0,1,0,0,0,0,0,1,1,0,0,0,1,1,0,1,1,0,1,1,0,1,0,1,0,0,0,1,1,1,0,0,1,1,0,0,0,0,0,1,1,0,1,1,0,0,0,1,1,0,1,1,1,0,1,1,0,1,1,1,0,0,0,1,1,0,0,0,0,0,0,1],[1,1,1,1,1,0,0,0,1,0,0,1,1,0,1,1,0,0,1,1,0,1,1,0,1,0,1,0,0,1,0,1,1,0,1,1,0,1,1,0,0,1,1,1,1,0,0,1,1,0,0,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,0,1,1,0,1,0,1,1,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,0,0,0,0,1,1,1,1,1],[1,0,0,1,0,0,0,0,0,1,1,0,0,0,1,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,0,0,1,1,0,1,1,1,0,1,1,0,1,0,1,1,0,1,0,0,0,0,1,0,0,1,0,1,0,0,0,1,1,0,1,1,0,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,0,1,1,0,0,1,1,1,0,1,0,1,1,1,0],[0,0,1,1,1,0,1,1,0,1,0,0,0,1,0,0,0,0,1,1,1,1,0,0,0,0,0,1,0,1,1,0,1,1,1,1,0,0,0,0,0,1,1,1,1,0,1,0,0,1,1,1,0,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,0,0,0,1,0,1,1,0,1,1,1,0,1,0,0,1,0,1,1,1,1,0,1,0,0,1,1,1,0,1,1,1],[0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,1,0,0,0,1,1,1,1,1,0,1,1,1,0,0,1,1,1,1,0,1,1,0,1,0,0,0,0,1,1,1,0,1,0,1,0,1,0,1,1,0,1,1,0,0,0,0,1,0,0,1,0,0,0,0,1,1,1,0,1,1,1,0,0,0,1,1,0,0,1,0,1,0,0,0,0,1,1,0,0,1],[1,0,1,1,1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,1,0,1,0,0,0,0,1,1,1,0,0,1,0,1,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0],[0,0,1,0,0,1,0,1,0,1,1,0,1,1,1,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,1,1,0,0,1,1,0,0,0,0,1,0,0,0,1,0,1,0,0,1,1,0,1,0,1,0,1,1,1,1,0,1,1,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0],[0,0,1,0,1,0,0,1,1,1,0,0,0,0,1,1,1,1,0,1,1,0,0,1,0,0,0,0,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,0,1,0,0,0,1,0,1,1,1,1,1,1,0,0,0,1,0,0,1,0,1,1,1,1,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,1,1,1,0,1,1,1,1,0,1,1,1,1],[1,0,1,0,1,0,0,1,0,1,0,1,1,1,1,1,0,0,1,1,0,1,1,1,0,1,1,0,0,1,1,1,1,0,1,0,0,0,0,0,1,0,1,1,0,0,1,0,1,1,1,1,0,1,0,0,1,1,1,0,1,0,1,0,1,0,1,0,0,1,0,0,1,0,0,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,0,0,1,0,0,1,1,1,0],[1,0,0,1,1,1,1,1,0,0,1,0,1,1,0,1,1,1,0,1,0,1,0,1,1,0,0,1,0,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,0,1,0,1,1,1,0,1,0,0,0,1,1,0,1,1,1,1,0,1,1,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1],[1,0,1,0,1,1,0,1,1,1,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,1,1,1,1,1,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,0,0,1,0,1,0,0,0,1,0,0,1,1,1,0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,1,1,1,1,0,1,0,1,1,0,0],[1,0,1,0,0,1,0,0,0,0,1,1,0,1,1,0,1,0,0,1,1,1,0,1,1,1,0,0,1,1,1,1,1,0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,0,0,1,1,1,0,1,0,0,0,1,1,1,0,0,0,0,1,1,0,0,1,0,0,1,0,1,0,1,1,0,1,1,0,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1,1,0],[0,1,0,0,1,0,1,1,0,1,0,1,1,0,1,1,0,1,1,0,0,1,1,1,0,1,1,1,0,0,0,1,0,0,0,0,0,0,1,1,0,1,1,1,0,1,0,0,0,0,1,1,1,1,0,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1,0,0,1,1,0,0,1,0,1,1,1,0,0,1,0,1,1,0,1,0,1,0,0],[0,1,1,0,1,0,0,0,0,0,1,0,1,1,0,1,1,0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,0,1,1,0,1,0,1,1,1,0,1,1,0,0,1,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,1,1,0,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,0,0],[1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,1,1,0,0,1,1,1,1,0,0,0,1,0,0,1,1,0,1,0,0,1,0,1,0,1,0,1,1,1,0,0,0,1,0,0,0,0,0,1,1,0,1,1,0,1,1,1,0,0,1,1,0,1,1,0,0,0,0,0,1,0,1,1,0,1,0,0,0,1,1,1,0,1,1,1,0,1,0,1,0,0,1,1,1,1],[1,0,1,1,0,1,1,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,1,1,1,0,1,0,0,1,1,0,1,1,1,0,0,1,0,1,1,1,1,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,1,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,1,0,1,1,1,0,0,1,1,0,1,0,1,1,0,0,1,1,0,0,0,0],[0,0,1,0,1,0,0,1,1,1,1,0,0,1,1,0,1,0,0,1,0,0,0,0,1,1,0,0,0,1,0,1,0,0,0,1,1,1,1,1,0,0,1,1,0,1,0,1,1,0,1,1,1,0,0,1,1,0,0,0,1,1,1,1,0,1,0,1,0,0,1,0,1,1,1,1,1,0,1,0,1,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,1,1,1,1],[0,0,0,1,0,1,1,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,1,0,1,1,1,1,1,0,0,0,1,0,1,0,1,1,1,0,0,1,0,1,0,1,1,1,0,0,0,1,0,1,0,0,1,1,0,0,0,0,1,1,0,1,1,0,0,1,1,0,1,0,1,0,0,1,1,0,0],[0,0,1,0,1,0,0,1,1,1,1,1,0,1,0,1,1,0,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,1,1,1,0,1,1,1,1,1,1,0,1,1,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,1,1,0,1,1,0,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,1,0],[1,1,0,1,0,0,0,1,1,1,1,0,0,0,1,1,0,1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,1,1,1,0,1,1,1,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,1,1,1,0,1,1,1,0,1,0,0,1,0,0,1,1,1,1,0,0,0,1,1,0,0,0,1],[0,1,0,0,0,1,1,1,1,0,0,1,1,1,1,0,1,0,0,0,0,1,1,1,0,1,0,1,1,0,0,1,1,0,0,1,0,0,0,1,0,1,0,1,0,0,1,1,0,0,0,0,0,1,0,0,1,0,1,1,1,0,0,1,0,1,0,0,0,0,0,0,1,0,0,1,0,1,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],[1,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,1,0,1,0,0,0,1,1,1,0,1,0,0,0,1,0,0,0,1,1,1,0,0,1,1,0,0,1,0,0,1,0,1,1,0,0,0,0,0,1,0,0,0,1,1,0,1,0,1,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1,1,0,0,0,1,0,0,0,1,0],[0,0,1,0,1,0,0,0,1,1,0,0,0,0,1,0,1,0,1,1,0,1,1,0,1,0,0,1,0,0,1,1,1,0,1,1,1,0,1,1,1,0,0,1,0,1,1,0,1,0,0,0,1,0,0,1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,1,0,1,1,0,0,1,0,0,0,0,1,1,0,1,1,1,1,0,0,1],[0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,1,0,0,1,0,0,1,1,0,0,0,1,1,0,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,0,0,1,0,0,0,1,0,1,1,1,1,1,1,0,1,1,0,0,1,1,1,0,1,0,0,1,0,0,1,1,0,0,0,1,0,1,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0],[1,0,1,1,1,1,1,0,0,1,1,0,0,0,0,0,1,0,1,1,1,1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,1,0,1,1,0,0,0,0,1,1,1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,1,1,0,0,0,0,0,1,0,0,0,1,1,0,0,1,1,1,0,0,0,1,0,0,1,0,0,0,0,1,1,1,0,0,0,1,1,0,0],[1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0,1,1,0,1,0,0,1,0,0,0,0,0,1,0,1,0,0,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1,0,0,1,0,1,1,0,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1,1,1,0,0,0,1,0],[1,0,0,1,1,1,1,0,1,0,1,1,1,0,1,1,0,1,0,1,1,0,1,1,0,1,1,1,0,0,0,1,0,0,0,1,1,1,1,0,0,1,0,0,0,0,0,1,1,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,0,0,0,1,1,0,0,0,1,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,1,1,0,0,0,1],[0,0,1,0,1,1,1,1,0,0,0,1,0,1,1,0,0,1,0,1,0,0,0,0,0,0,0,1,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,1,1,0,0,1,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,1,1,0,1,0,1,1,0,1,0,0,0,1,1,1,0,0,0,1,0,0,1,0,1,0],[1,1,1,1,0,1,0,1,0,0,0,1,1,1,0,0,1,0,1,1,1,1,0,0,1,1,0,1,1,0,0,1,0,0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,1,0,0,1,1,0,1,0,1,1,1,0,0,1,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,0,1,0,1,1,1,0,0,1,1,0],[1,1,1,1,0,0,1,1,0,0,1,0,1,0,0,1,1,1,0,1,0,0,0,1,1,1,1,0,1,1,1,0,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,0,1,0,0,0,0,1,1,0,0,0,1,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,1,0,0,1,1,1,1,0,1,1,1,1,1,1,0,0,1,0,1,0,1,1,0,1,1,1],[0,0,0,0,0,1,0,0,0,0,1,0,1,1,0,1,1,1,0,0,0,0,0,1,1,0,1,1,1,1,1,0,0,1,1,0,1,1,1,0,0,1,1,1,0,1,1,0,1,0,1,1,0,0,1,0,0,1,1,1,0,0,0,1,1,0,1,1,0,0,1,1,0,1,0,0,0,1,0,0,1,1,1,0,0,0,0,1,0,0,1,0,0,0,1,0,1,1,1,1],[1,1,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,1,1,0,0,1,1,0,1,1,0,0,1,1,1,0,0,1,1,1,0,1,1,0,0,0,1,0,0,1,0,1,0,0,1,1,1,0,0,1,1,0,1,0,0,1,1,1,0,0,0,0,0,1,0,0,0,1,0,1,1,1,1,0,0,0,1,0,1,1,0,1,1,0,1,1,0,1,0,1,0,0,1,0],[0,1,0,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,0,0,1,0,1,1,0,0,1,1,1,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,1,0,1,1,1,0,1,1,0,1,0,1,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1,1,0,0,0,0,1,1,0,1,0],[1,1,1,1,1,1,0,0,0,1,1,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,1,0,1,1,0,1,0,0,1,1,1,1,0,1,1,1,0,1,0,1,0,0,1,0,0,1,0,1,0,0,0,1,1,1,0,0,1,0,1,0,1,1,0,1,1,0,1,1,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0],[0,0,1,0,0,0,1,1,0,0,1,0,1,1,0,0,1,1,1,1,1,1,0,1,0,1,0,0,1,1,1,0,1,0,0,1,0,0,1,0,0,1,0,1,1,1,0,1,1,0,0,1,0,1,1,1,0,0,0,1,0,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,1,1,0,1,0,0,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,1],[1,1,1,1,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,1,1,1,0,1,0,0,0,0,1,0,0,0,1,0,0,1,1,0,1,0,1,1,0,0,0,1,0,1,1,1,0,0,1,0,1,1,1,0,0,1,1,1,0,1,0,1,0,0,0,1,0,1,1,1,0,0,1,1,1,0,1,0,0,0,1,1,1,0,1,0,0,1,1,0,0],[0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1,1,1,1,1,1,1,0,1,1,0,1,0,0,1,1,1,0,1,0,1,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0],[1,0,1,0,0,0,0,0,1,1,0,0,0,1,0,1,1,0,1,1,1,1,0,0,0,1,1,1,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,0,0,1,1,0,1,0,0,1,1,1,0,1,1,0,0,0,1,0,1,0,1,1,1,0,1,0,0,1,1,1,1,1,0,1,1],[1,1,1,1,0,1,0,1,1,1,0,0,1,1,0,1,1,0,1,1,1,0,1,0,0,0,1,1,0,1,0,1,0,1,1,0,1,1,0,0,1,1,0,1,1,1,1,1,0,0,1,1,1,0,0,0,0,1,1,0,0,1,0,0,1,0,0,0,0,1,1,1,1,1,1,0,0,1,1,0,0,0,0,1,0,1,1,1,0,1,1,0,1,0,0,0,0,0,1,0],[1,1,0,0,1,1,0,1,1,0,0,1,1,1,0,1,1,1,1,1,1,0,0,1,1,1,1,0,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0,1,0,0,0,1,1,1,0,1,0,0,0,1,0,1,1,1,0,1,0,0,0,0,1,1,0,0,1,1,0,1,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0],[0,0,0,0,1,1,1,1,0,0,0,1,0,0,1,1,0,0,1,0,0,1,1,0,1,1,0,0,0,1,0,1,1,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1,1,1,0,1,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,1,0,1,0,1,1,1,0,1,1],[0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1,1,0,0,0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,0,1,1,1,1,1,0,0,1,1,1,0,1,1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,1,1,0,1,0,0,0,1,1,0,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,1,1,1,0,1,0,1],[1,0,0,0,0,0,1,0,0,0,0,1,1,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,0,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,1,0,1,1,1,1,0,1,0,1],[1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,0,1,0,1,0,1,1,0,1,0,1,1,1,1,1,0,1,0,1,0,0,1,1,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,0,1,1,1,0,1,1,0,1,0,0,0,0,0,1,1,0,1,1],[0,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,0,1,0,1,1,0,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,1,1,0,1,1,0,0,1,0,1,0,0,1,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,0,1,0,0],[1,0,0,0,1,0,0,1,0,1,1,0,0,1,0,1,1,1,1,0,0,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1,1,0,1,1,0,0,0,1,0,1,1,1,0,1,1,0,0,1,1,0,0,1,0,0,1,0,1,1,1,1,0,1,1,0,0,1,0,0,1,1,1,0,0,0,1,1,0,1,0,0,0,0,1,1,1,0,0,1,1,1,1,0,1,1],[0,0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,0,1,1,1,1,0,0,0,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,1,0,1,1,1,1,1,0,1,0,0,0,0,1,1,0,0,1,0,0,1,0,0,0,1,0,1,1,1,1,1,0,1,1,0,0,0,1,0,1,0,1,0,1,1,1,1,1,1,0,1,1,0,0,1,1,0,0,0],[1,0,1,0,0,1,0,0,0,1,1,0,0,0,0,1,1,0,1,1,1,1,0,0,0,0,1,0,1,1,1,0,0,1,0,0,0,0,0,1,1,0,1,1,1,0,1,0,0,1,1,1,1,1,0,1,1,1,0,0,0,1,1,1,1,0,0,1,1,0,1,1,1,1,0,0,0,0,1,1,0,0,1,1,0,0,0,0,1,0,1,1,0,0,1,1,1,1,1,0],[0,0,1,1,1,1,0,0,0,0,0,0,0,1,0,0,1,0,1,1,1,0,1,0,0,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,1,0,1,0,0,1,1,1,1,0,0,1,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,1,1,1,0,1,0,0,0,0,0,0,1,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1],[0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0,0,0,1,1,1,0,1,1,1,0,0,1,0,1,0,1,0,0,0,1,1,1,1,0,1,1,1,0,1,1,0,1,1,1,0,0,0,0,0,1,0,0,1,0,0,0,0,1,1,1,0,0,1,1,0,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1,0,1,1,0,1,0,1,0,0,1,1],[1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,1,0,0,0,1,0,0,1,0,1,1,0,1,0,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,1,1,0,0,0,1,0,0,1,1,1,0,1,0,0,1,0,1,1,1,1,1,1,0,1,1,1,1,0,0,1,0],[0,0,1,1,1,1,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,1,1,0,1,0,0,1,1,0,0,0,0,0,1,0,0,1,0,1,1,1,1,1,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,1,1,0,0,1,1,1,0,1,0,1,1,0,1,0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1],[0,0,0,0,1,0,0,1,1,1,1,0,0,1,1,0,0,0,0,0,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,0,1,0,0,0,1,1,0,0,1,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,1,1,1,0,1,1,1,0,1,0,0,1,0,1,0,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1],[1,0,0,1,1,0,1,1,0,0,0,0,1,1,0,0,1,0,1,1,1,0,0,0,0,0,1,0,1,1,1,1,1,0,0,1,0,1,1,1,1,0,0,0,0,0,1,1,0,1,1,0,0,1,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,1,1,1,0,1,1,0,0,1,0,0,0,0,1,0,0,0,1,1,1,0,0,1,1,0,1,1,1,0],[0,1,1,0,1,0,0,1,1,1,0,0,0,1,0,0,1,1,1,1,0,0,1,1,0,1,1,0,0,0,1,0,1,1,1,1,0,0,0,1,1,1,0,1,0,1,1,1,0,0,1,1,1,0,0,1,1,0,0,1,1,1,0,1,0,1,1,0,0,1,0,1,1,1,0,1,0,1,0,1,0,0,0,0,1,0,1,1,1,0,0,0,0,1,0,0,0,1,0,1],[1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,0,0,1,0,1,1,0,0,1,1,0,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,1,1,1,1,0,1,0,0,1,1,1,1,1,0,1,1,1,0,1,0,0,0,1,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,1,0,0,1,0,1,1,0,1,1,0,0,0,0,1,1,0,1,0,1,1],[0,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,0,1,1,1,1,1,0,1,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,1,0,0,1,1,1,1,0,1,0,1,0,0,0,0,1,1,0,1,1,0,0,0,0,1],[1,1,1,0,0,1,0,1,0,1,0,0,0,0,1,0,0,0,1,0,1,1,1,1,0,0,1,1,1,0,1,1,1,1,1,1,0,1,1,1,0,0,1,1,0,0,1,1,0,0,1,1,1,0,0,1,0,1,0,1,1,1,1,0,1,1,1,0,0,0,0,1,1,1,0,0,1,0,1,1,1,1,0,1,0,0,0,0,1,0,0,0,0,1,0,1,1,1,0,0],[1,1,0,1,0,1,1,1,0,1,0,0,1,0,1,0,1,1,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1,1,1,0,1,1,1,1,0,1,0,0,0,1,1,0,1,1,1,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,1,1,1,0,1,0,1,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,0,0,1,0,1,0,1,0],[0,0,1,1,0,1,1,0,1,1,1,1,0,0,0,1,0,1,0,1,1,0,1,1,0,1,1,1,1,0,0,0,1,1,1,1,1,0,1,1,0,0,0,1,0,0,1,1,1,1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,1,1,1,1,0,0,0,1,1,1,1,0,1,1,0,0,0,0,1,0,1,1,1],[1,0,1,0,0,1,1,1,0,0,0,1,0,0,1,0,0,1,1,1,0,1,1,1,0,0,1,0,1,0,0,0,0,1,0,0,1,0,1,1,0,0,0,0,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,0,1,0,0,0,1,0,1,1,1,1,1,0,0,1,0,1,1,1,1,1,0,1,1,1,0,0,0,0,1,0,0,1,1,1,1,1,1,0,1,1],[0,0,1,1,0,1,1,0,0,1,1,1,1,0,0,0,1,1,0,1,1,1,0,1,1,0,1,1,0,0,0,1,1,1,1,0,1,1,1,1,1,0,1,0,0,0,1,0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,1,0,1,0,1,1,1,0,0,1,0,0,1,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,1,1,0],[1,0,1,0,1,0,1,0,0,0,1,0,1,1,0,0,0,0,1,1,1,0,0,0,1,1,0,1,0,0,0,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,0,1,0,1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,1,0,1,0,1,0,1,1,1,0,0,0,0,1,1,1,0,1,1,1,0,1,0,0,0],[1,1,0,0,1,0,0,1,1,1,1,0,1,1,1,1,0,0,0,0,1,0,0,1,1,0,0,1,1,1,0,0,1,0,0,1,0,0,1,1,1,0,0,1,1,1,1,0,0,0,1,1,1,0,0,1,0,1,0,1,1,0,1,0,0,0,0,0,1,1,0,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,1,1,1,0,1],[0,1,1,0,0,0,0,1,1,0,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,0,0,1,1,0,1,0,0,1,1,1,0,1,0,0,1,0,0,0,0,1,1,1,0,1,0,0,1,0,0,1,0,1,0,0,0,0,0,0],[0,1,0,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,0,0,1,0,0,1,1,1,1,0,0,1,0,1,1,1,0,1,0,0,0,0,0,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,0,1,0,1,0,0,0,0,1,0,1,1,1,0,0,1,1,0,0,1,1,0,1,1,1,1,0,0,1,1],[1,0,1,0,1,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,1,1,1,0,1,1,1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,1,0,0,1,1,0,1,1,1,0,0,0,1,0,0,1,0,0,1,1,0,0,0,0,1,1,1,0,0,1,1,1,0,0,1,0,0,0,1,1,1,1,1,0,0,0,0,0,1,0,0,1,1,1,1],[0,0,0,0,1,0,1,1,0,1,0,1,1,0,0,0,0,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,1,0,1,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1,0,1,1,1,0,1,0,1,1,0,0,0,0,1,1,0,1,1,1,1,1,1,0,0],[0,1,0,0,1,1,0,1,1,0,0,0,0,0,0,0,1,0,1,0,1,1,0,1,1,0,1,0,1,1,0,0,1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,1,1,0,1,0,0,1,1,1,1,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,0,0,1,1,0,1,0,1],[1,0,0,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,1,0,1,0,1,1,1,0,1,1,0,1,1,1,1,1,1,0,1,1,1,0,0,1,1,0,0,1,1,1,0,0,0,1,0,1,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,1,1,0,0,1,0,1,0,1,1,1,0,0,0,1,0,0,1,0,1,1,0,1,1,1],[1,0,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,1,1,1,0,0,0,1,0,1,0,0,0,1,1,1,0,1,1,0,1,0,0,0,0,1,0,1,0,1,0,1,0,0,1,1,0,1,0,1,1,0,1,1,0,0,1,0,0,0,1,0,1,1,0,0,0,1,1,0,1,1,1,0,1,1,0,1,0],[1,0,1,0,1,0,0,0,1,0,0,0,0,1,1,0,0,1,1,1,1,1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,1,0,1,0,1,1,0,0,0,1,0,1,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,1,1,1,0,1,1,0,1,0,0,0,1,0,1,0,1,1,1,1,0,1,0,0,1,0,0,1,1,1,0,0,1,1],[1,0,0,1,0,1,1,1,0,0,0,1,0,1,0,0,1,1,0,1,0,1,1,0,1,1,0,0,1,0,1,0,0,0,0,1,1,1,0,0,1,0,0,1,1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,0,1,1,0,0,1,1,1,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,1,1,1,0,0],[0,1,0,0,1,0,1,0,0,0,0,0,1,0,1,1,0,1,1,0,1,1,1,1,1,1,0,0,0,1,0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,1,1,0,0,1,0,0,0,0,0,1,0,0,1,1,0,1,0,1,1,1,1,1],[1,1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,1,0,0,0,1,1,1,0,1,1,1,0,0,0,0,1,0,1,0,1,1,0,1,1,0,1,1,1,0,1,0,0,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,1,0,1,1,1,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,1,0,0,1,0,1,1],[0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,1,1,0,0,1,1,1,0,0,1,0,0,1,0,1,1,0,0,1,0,1,0,0,0,1,1,1,1,1,1,1,0,1,1,1,0,0,0,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,0,1,1,0,0,0,1,1,0,1,0,0],[1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,0,0,0,0,1,1,0,1,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,1,0,1,1,1,1,1,1,0,0,1,0,0,0,0,1,1,1,1,0,1,0,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,0,0,1,0,1,1,0,0,1,1,1,0,1,1,0],[0,0,0,1,0,1,1,0,1,1,1,1,0,1,1,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,1,0,1,1,0,0,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,0,1,1,0,0,1,1,0,1,1,0,0,0,1,1,0,0,1,0,1,1,0,1,0,1,1,1,0,0,1,0,1,0,0,0,1,0,1,1],[0,1,0,0,1,0,0,1,0,1,1,1,0,1,1,1,1,0,0,0,1,1,0,0,1,0,1,0,0,1,1,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,1,1,0,1,0,0,1,1,0,0,1,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,0,0,1,1,0,0,1,1,0,1,1,1,0,1,1,1,1,0,0,1,0,1,1,1,0,1,1,1],[1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,1,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,1,0,1,0,0,1,1,0,1,0,1,1,0,0,0,0,1,1,1,1,1,0,0,1,0,1,1,0,1,1,1,0,1,1,0,0,0,0,1,0,1,1,1,0,0,1,1,1,1,1,0,0,1,0,0,1,1,0,1,0,1,0,1,1,0,1,0,0],[1,1,1,0,0,1,1,1,1,0,1,1,1,1,0,0,0,1,1,1,0,1,1,1,0,1,1,0,0,0,0,0,0,0,1,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,0,1,1,1,1,0,0,0,0,1,1,0,1,0,0,1,0,1,0,1,1,0,0,1,0,1,1,0,0],[1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,0,0,1,0,1,1,1,0,1,0,0,1,0,1,1,1,0,1,0,0,1,0,0,0,1,0,1,1,1,0,0,1,0,0,0,0,0,1,1,1,1,1,0,0,0,1,0,1,0,0,1,0,0,0,1,1,0,1,0,1,0,1,0,1,0,0,1,1,1,0,1,1,0,0,0,0,1,0,0,1,1,0,0,1,0],[0,1,0,1,1,0,1,0,0,0,1,1,0,0,1,0,1,0,0,0,1,0,1,1,0,1,0,0,0,1,1,0,0,1,1,0,0,1,0,0,1,0,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,0,1,0,1,0,0,1,1,0,1,0,1,0,0,0,0,0,0,1,1,1,0,1,1,1,0,0,1,0,1,1,1,1,1,0,1,1,1],[0,1,1,0,1,1,0,1,1,0,0,1,1,0,0,0,0,1,0,0,1,0,0,0,0,1,1,0,0,1,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,1,1,1,1,1,0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,1,0,1,1,0,1,0,0,1,1,0,1,1,0,0,1,1,0,1,0,0,0,0,0,1,1,1,0,1,0,1,0],[1,0,1,0,0,1,0,0,0,1,1,1,0,0,1,1,0,0,1,1,1,1,1,1,0,0,1,1,0,0,1,0,0,1,0,1,0,0,1,0,1,1,1,0,0,1,1,0,1,0,0,1,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,1,1,0,0,1,1,1,0,1,0,0,0,0],[1,0,0,1,1,0,1,1,1,0,1,0,1,0,1,1,1,1,0,0,0,1,0,1,0,0,0,1,1,1,1,1,0,1,1,0,0,1,1,0,1,1,0,1,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,1,1,1,0,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,1,1,0,0,0,0,1,0,1,1,0,1,1,1,1,0,0,0,0,1]]
    target = 0
    assert Solution().numSubmatrixSumTarget(matrix, target) == 15691
