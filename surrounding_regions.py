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

        def bfs(r, c, liberty):
            """BFS to determine connected component."""
            queue = collections.deque()
            queue.append((r, c))
            while queue:
                r0, c0 = queue.popleft()
                liberty[r0][c0] = True
                for r1, c1 in neighbors(r0, c0):
                    if board[r1][c1] == 'O' and not liberty[r1][c1]:
                        queue.append((r1, c1))

        def check(r, c, liberty):
            """Use the BFS if (r, c) is a O on the edge of the board."""
            if board[r][c] == 'O' and not liberty[r][c]:
                bfs(r, c, liberty)

        liberty = [[False for _ in row] for row in board]

        # Top row
        for c, _ in enumerate(board[0]):
            check(0, c, liberty)

        # Bottom row
        N = len(board)
        for c, _ in enumerate(board[N-1]):
            check(N-1, c, liberty)

        # Left/right column
        M = len(board[0])
        for r, _ in enumerate(board[1:-1]):
            check(r, 0, liberty)
            check(r, M-1, liberty)

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