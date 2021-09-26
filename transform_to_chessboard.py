"""
LeetCode :: September Challenge :: Transform to Chessboard
jramaswami

REF: https://www.youtube.com/watch?v=pPks_UrfETo
"""


class Solution:

    def movesToChessboard(self, board):
        board_length = len(board)
        col_moves_needed = 0
        row_moves_needed = 0
        ones_in_first_row = 0
        ones_in_first_col = 0

        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if ((board[0][0] ^ board[r][0]) ^ (board[r][c] ^ board[0][c])) == 1:
                    return -1

        for i, _ in enumerate(board):
            ones_in_first_row += board[0][i]
            ones_in_first_col += board[i][0]

            if board[i][0] == i % 2:
                row_moves_needed += 1
            if board[0][i] == i % 2:
                col_moves_needed += 1

        if ones_in_first_row < (board_length // 2) or ones_in_first_row > ((board_length + 1) // 2):
            return -1
        if ones_in_first_col < (board_length // 2) or ones_in_first_col > ((board_length + 1) // 2):
            return -1

        if board_length % 2:
            if col_moves_needed % 2:
                col_moves_needed = board_length - col_moves_needed
            if row_moves_needed % 2:
                row_moves_needed = board_length - row_moves_needed
        else:
            col_moves_needed = min(col_moves_needed, board_length - col_moves_needed)
            row_moves_needed = min(row_moves_needed, board_length - row_moves_needed)

        return (col_moves_needed + row_moves_needed) // 2


def test_1():
    board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
    assert Solution().movesToChessboard(board) == 2


def test_2():
    board = [[1,0],[1,0]]
    assert Solution().movesToChessboard(board) == -1


def test_3():
    board = [[1,1,0],[0,0,1],[0,0,1]]
    assert Solution().movesToChessboard(board) == 2
