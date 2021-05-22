"""
Leet Code :: May 2021 Challenge :: N-Queens
jramaswami
"""


from typing import *
from collections import namedtuple
from itertools import combinations


Queen = namedtuple('Queen', ['rank', 'file'])


def make_board(queens, n):
    """Return a string representation of the board."""
    board = [['.' for _ in range(n)] for _ in range(n)]
    for queen in queens:
        board[queen.rank][queen.file] = 'Q'
    return ["".join(row) for row in board]


def peaceful(queens):
    """Return True if no queen is under threat."""
    # Base case: only 1 queen is always safe.
    if len(queens) <= 1:
        return True
    for q1, q2 in combinations(queens, 2):
        # Make sure there are no more than 1 queen rank and file.
        if q1.rank == q2.rank or q1.file == q2.file:
            return False
        # Check diagonal attacks
        if abs(q1.rank - q2.rank) == abs(q1.file - q2.file):
            return False
    return True


def solve(queens, n, acc):
    if len(queens) == n:
        acc.append(list(queens))
        return

    for chess_rank in range(n):
        queens.append(Queen(chess_rank, len(queens)))
        if peaceful(queens):
            solve(queens, n, acc)
        queens.pop()


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        acc = []
        solve([], n, acc)
        return [make_board(t, n) for t in acc]


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
