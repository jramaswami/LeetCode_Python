"""
LeetCode :: April 2022 Challenge :: 289. Game of Life
jramaswami
"""


class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        OFFSETS = (
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        )

        def inbounds(r, c):
            return r >= 0 and r < len(board) and c >= 0 and c < len(board[r])

        def neighbors(r, c):
            for dr, dc in OFFSETS:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        def alive(r, c):
            return board[r][c] > 0

        def live_neighbors(r, c):
            return sum(alive(r0, c0) for r0, c0 in neighbors(r, c))

        for r, row in enumerate(board):
            for c, curr in enumerate(row):
                ln = live_neighbors(r, c)
                if curr != 0:
                    if ln < 2:
                        # Any live cell with fewer than two live neighbors dies
                        # as if caused by under-population.
                        board[r][c] = 2
                    elif 2 <= ln <= 3:
                        # Any live cell with two or three live neighbors lives
                        # on to the next generation.
                        pass
                    else:
                        # Any live cell with more than three live neighbors
                        # dies, as if by over-population.
                        board[r][c] = 2
                else:
                    # Any dead cell with exactly three live neighbors becomes a
                    # live cell, as if by reproduction.
                    if ln == 3:
                        board[r][c] = -1

        for r, row in enumerate(board):
            for c, curr in enumerate(row):
                if curr == 2:
                    board[r][c] = 0
                elif curr == -1:
                    board[r][c] = 1


def test_1():
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    expected = [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
    Solution().gameOfLife(board)
    assert board == expected


def test_2():
    board = [[1,1],[1,0]]
    expected = [[1,1],[1,1]]
    Solution().gameOfLife(board)
    assert board == expected
