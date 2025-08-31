"""
LeetCode
37. Sudoku Solver
August 2025 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_values = collections.defaultdict(set)
        col_values = collections.defaultdict(set)
        box_values = collections.defaultdict(set)

        def get_box_key(r, c):
            return (3 * (r // 3), 3 * (c // 3))

        def add_value(r, c, val):
            row_values[r].add(val)
            col_values[c].add(val)
            box_values[get_box_key(r, c)].add(val)
            board[r][c] = val

        def remove_value(r, c, val):
            row_values[r].remove(val)
            col_values[c].remove(val)
            box_values[get_box_key(r, c)].remove(val)
            board[r][c] = '.'

        def is_valid_value(r, c, val):
            return (
                val not in row_values[r] and
                val not in col_values[c] and
                val not in box_values[get_box_key(r, c)]
            )

        cells_to_fill = []
        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if val == '.':
                    cells_to_fill.append((r, c))
                else:
                    add_value(r, c, val)

        def rec(i):
            if i >= len(cells_to_fill):
                return True
            r, c = cells_to_fill[i]
            # Try every value
            for cell_value in '123456789':
                # If it is a valid value for the cell
                if is_valid_value(r, c, cell_value):
                    add_value(r, c, cell_value)
                    result = rec(i+1)
                    if result:
                        return result
                    remove_value(r, c, cell_value)

        rec(0)


def test_1():
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    expected = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
    Solution().solveSudoku(board)
    assert board == expected


if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    Solution().solveSudoku(board)
