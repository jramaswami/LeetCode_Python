"""
LeetCode
2352. Equal Row and Column Pairs
June 2023 Challenge
jramaswami
"""


from typing import *


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Simplest possible solution

        def row_same_as_col(row_index, col_index):
            for off in range(len(grid)):
                if grid[row_index][off] != grid[off][col_index]:
                    return False
            return True


        soln = 0
        for r, _ in enumerate(grid):
            for c, _ in enumerate(grid[0]):
                if row_same_as_col(r, c):
                    soln += 1
        return soln


def test_1():
    grid = [[3,2,1],[1,7,6],[2,7,7]]
    expected = 1
    assert Solution().equalPairs(grid) == expected


def test_2():
    grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    expected = 3
    assert Solution().equalPairs(grid) == expected