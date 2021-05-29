"""
Leet Code :: May 2021 Challenge :: N-Queens II
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


def solve(queens, n):
    if len(queens) == n:
        return 1

    soln = 0
    for chess_rank in range(n):
        queens.append(Queen(chess_rank, len(queens)))
        if peaceful(queens):
            soln += solve(queens, n)
        queens.pop()
    return soln


class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        return solve([], n)


def test_1():
    assert Solution().totalNQueens(4) == 2


def test_2():
    assert Solution().totalNQueens(1) == 1