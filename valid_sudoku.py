"""
LeetCode :: 36. Valid Sudoku
November 2022 Challenge
jramaswami
"""


from typing import *


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def col_generator(c):
            for r in range(9):
                yield board[r][c]

        def row_generator(r):
            for k in board[r]:
                yield k

        def box_generator(r0, c0):
            for r in range(r0, r0+3):
                for c in range(c0, c0+3):
                    yield board[r][c]

        def valid_set(generator):
            visited = set()
            for k in generator:
                if k != '.':
                    if k in visited:
                        return False
                    visited.add(k)
            return True

        for r, _ in enumerate(board):
            if not valid_set(row_generator(r)):
                # print("invalid row:", r)
                return False
        for c, _ in enumerate(board[0]):
            if not valid_set(col_generator(c)):
                # print("invalid col:", c)
                return False
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                # print("invalid box:", r, c)
                if not valid_set(box_generator(r, c)):
                    return False
        return True



def test_1():
    board = [["5","3",".",".","7",".",".",".","."] ,["6",".",".","1","9","5",".",".","."] ,[".","9","8",".",".",".",".","6","."] ,["8",".",".",".","6",".",".",".","3"] ,["4",".",".","8",".","3",".",".","1"] ,["7",".",".",".","2",".",".",".","6"] ,[".","6",".",".",".",".","2","8","."] ,[".",".",".","4","1","9",".",".","5"] ,[".",".",".",".","8",".",".","7","9"]]
    expected = True
    assert Solution().isValidSudoku(board) == expected


def test_2():
    board = [["8","3",".",".","7",".",".",".","."] ,["6",".",".","1","9","5",".",".","."] ,[".","9","8",".",".",".",".","6","."] ,["8",".",".",".","6",".",".",".","3"] ,["4",".",".","8",".","3",".",".","1"] ,["7",".",".",".","2",".",".",".","6"] ,[".","6",".",".",".",".","2","8","."] ,[".",".",".","4","1","9",".",".","5"] ,[".",".",".",".","8",".",".","7","9"]]
    expected = False
    assert Solution().isValidSudoku(board) == expected
