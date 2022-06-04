"""
Leet Code :: June 2022 Challenge :: N-Queens
jramaswami
"""


import collections


class Solver:
    def __init__(self, dim):
        self.dim = dim
        self.rows = [-1 for _ in range(dim)]
        self.neg_diag = collections.defaultdict(bool)
        self.pos_diag = collections.defaultdict(bool)
        self.solns = []

    def _peaceful(self, row, col):
        # I can place a queen at (row, col) if:
        # (1) That row is not already taken.
        if self.rows[row] != -1:
            return False
        # (2) The neg_diag is not occupied.
        if self.neg_diag[row - col] == True:
            return False
        # (3) The pos_diag is not occupied.
        if self.pos_diag[row + col] == True:
            return False
        return True

    def _render_board(self):
        board = [["." for _ in range(self.dim)] for _ in range(self.dim)]
        for row, col in enumerate(self.rows):
            board[row][col] = "Q"
        return ["".join(row) for row in board]

    def _solve(self, col):
        # Base case
        if col >= self.dim:
            # Add board
            self.solns.append(self._render_board())
            return

        for row in range(self.dim):
            if self._peaceful(row, col):
                self.rows[row] = col
                self.neg_diag[row - col] = True
                self.pos_diag[row + col] = True
                self._solve(col+1)
                self.rows[row] = -1
                self.neg_diag[row - col] = False
                self.pos_diag[row + col] = False

    def solve(self):
        self._solve(0)
        return self.solns


class Solution:
    def solveNQueens(self, n):
        solver = Solver(n)
        return solver.solve()


def test_1():
    expected = [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    result = Solution().solveNQueens(4)
    assert sorted(expected) == sorted(result)


def test_2():
    expected = [["Q"]]
    result = Solution().solveNQueens(1)
    assert sorted(expected) == sorted(result)


def test_3():
    expected = [["Q....","..Q..","....Q",".Q...","...Q."],["Q....","...Q.",".Q...","....Q","..Q.."],[".Q...","...Q.","Q....","..Q..","....Q"],[".Q...","....Q","..Q..","Q....","...Q."],["..Q..","Q....","...Q.",".Q...","....Q"],["..Q..","....Q",".Q...","...Q.","Q...."],["...Q.","Q....","..Q..","....Q",".Q..."],["...Q.",".Q...","....Q","..Q..","Q...."],["....Q",".Q...","...Q.","Q....","..Q.."],["....Q","..Q..","Q....","...Q.",".Q..."]]
    result = Solution().solveNQueens(5)
    assert sorted(expected) == sorted(result)
