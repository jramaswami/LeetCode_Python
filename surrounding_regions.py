"""
LeetCode :: November Challenge :: 130. Surrounded Regions
jramaswami
"""


import collections


class Solution:

    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """

        def inbounds(r, c):
            """Return True if (r, c) is inside the board."""
            return r >= 0 and c >= 0 and r < len(board) and c < len(board[r])

        def neighbors(r, c):
            """Generator for 4-neighborhood."""
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        queue = collections.deque()
        liberty = [[False for _ in row] for row in board]

        # Gather Os on the edge of the board.
        # Top row
        for c, _ in enumerate(board[0]):
            if board[0][c] == 'O':
                queue.append((0, c))
                liberty[0][c] = True

        # Bottom row
        N = len(board)
        for c, _ in enumerate(board[N-1]):
            if board[N-1][c] == 'O':
                queue.append((N-1, c))
                liberty[N-1][c] = True

        # Left/right column
        M = len(board[0])
        for r, _ in enumerate(board[1:-1], start=1):
            if board[r][0] == 'O':
                queue.append((r, 0))
                liberty[r][0] = True
            if board[r][M-1] == 'O':
                queue.append((r, M-1))
                liberty[r][M-1] = True

        # BFS to determine Os connected to the edge.
        while queue:
            r, c = queue.popleft()
            for r0, c0 in neighbors(r, c):
                if board[r0][c0] == 'O' and not liberty[r0][c0]:
                    queue.append((r0, c0))
                    liberty[r0][c0] = True

        # Make captures
        for r, row in enumerate(board):
            for c, _ in enumerate(row):
                if liberty[r][c]:
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'


def test_1():
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    expected = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    Solution().solve(board)
    assert board == expected


def test_2():
    board = [["X"]]
    expected = [["X"]]
    Solution().solve(board)
    assert board == expected


def test_3():
    """WA"""
    board = [["X","O","X"],["O","X","O"],["X","O","X"]]
    expected = [["X","O","X"],["O","X","O"],["X","O","X"]]
    Solution().solve(board)
    assert board == expected