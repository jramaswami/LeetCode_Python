"""
LeetCode :: June 2021 Challenge :: Out of Boundary Paths
jramaswami
"""


from collections import defaultdict


class Solution:
    def findPaths(self, grid_height, grid_width, max_move, start_row, start_column):
        MOD = pow(10, 9) + 7

        def neighbors(r, c):
            """Neighbors in the four directions."""
            moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in moves:
                r0 = r + dr
                c0 = c + dc
                yield (r0, c0)

        def is_inbounds(r, c):
            """Return True if cell is inside the grid."""
            return r >= 0 and c >= 0 and r < grid_height and c < grid_width

        soln = 0

        # dp dicts will hold the number of ways to get to a given cell.
        prev_dp = defaultdict(int)
        curr_dp = defaultdict(int)
        # There is initially one way to reach the start position.
        prev_dp[(start_row, start_column)] = 1

        # Tick over time, making moves from all reachable cells.
        for tick in range(max_move):

            # For all the cells reachable in the previous round ...
            for (r, c), k in prev_dp.items():
                # For all the neighbor of a cell from the previous round ...
                for r0, c0 in neighbors(r, c):
                    if is_inbounds(r0, c0):
                        # Since there were k ways to reach (r, c), add k to the
                        # number of ways to reach (r0, c0).
                        curr_dp[(r0, c0)] = (curr_dp[(r0, c0)] + k) % MOD
                    else:
                        # Since there were k ways to reach (r, c), there are
                        # k more ways to go out of bounds.
                        soln = (soln + k) % MOD

            prev_dp, curr_dp = curr_dp, defaultdict(int)

        return soln


def test_1():
    m = 2
    n = 2
    max_move = 2
    start_row = 0
    start_column = 0
    expected = 6
    assert Solution().findPaths(m, n, max_move, start_row, start_column) == expected


def test_2():
    m = 1
    n = 3
    max_move = 3
    start_row = 0
    start_column = 1
    expected = 12
    assert Solution().findPaths(m, n, max_move, start_row, start_column) == expected


def test_3():
    m = n = max_move = 50
    start_row = start_column = 0
    expected = 678188903
    assert Solution().findPaths(m, n, max_move, start_row, start_column) == expected


def test_4():
    m = n = max_move = 50
    start_row = start_column = 25
    expected = 276775132
    assert Solution().findPaths(m, n, max_move, start_row, start_column) == expected
