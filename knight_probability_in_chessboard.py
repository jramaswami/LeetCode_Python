"""
LeetCode
688. Knight Probability in Chessboard
jramaswami
"""


import functools


class Solution:

    OFFSETS = (
            (2, -1), (1, 2), (-1, -2), (2, 1),
            (-2, -1), (-2, 1), (1, -2), (-1, 2)
    )

    P = (1.0 / 8.0)

    def knightProbability(self, n: int, k: int, init_row: int, init_col: int) -> float:

        def out_of_bounds(row, col):
            return (
                row < 0 or col < 0 or
                row >= n or col >= n
            )

        @functools.cache
        def rec(row, col, moves_left):
            print(f"rec({row=}, {col=}, {moves_left=})")
            if moves_left < 0:
                return 0

            if out_of_bounds(row, col):
                return 1

            return sum(
                Solution.P * rec(row + dr, col + dc, moves_left - 1)
                for dr, dc in Solution.OFFSETS
            )

        p_out_of_bounds = rec(init_row, init_col, k)
        return 1.0 - p_out_of_bounds


EPS = pow(10, -6)


def test_1():
    n = 3
    k = 2
    row = 0
    column = 0
    expected = 0.06250
    assert abs(Solution().knightProbability(n, k, row, column) - expected) < EPS


def test_2():
    n = 1
    k = 0
    row = 0
    column = 0
    expected = 1.0
    assert abs(Solution().knightProbability(n, k, row, column) - expected) < EPS