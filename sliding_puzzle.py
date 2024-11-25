"""
LeetCode
773. Sliding Puzzle
November 2024 Challenge
jramaswami
"""


from typing import List
import collections


class Solution:
    def slidingPuzzle(self, initial_board: List[List[int]]) -> int:

        def find_zero(board):
            for r, row in enumerate(board):
                for c, val in enumerate(row):
                    if val == 0:
                        return r, c

        def inbounds(r, c, board):
            return r >= 0  and r < len(board) and c >= 0 and c < len(board[r])

        def swap(r, c, r0, c0, board):
            board0 = list(list(row) for row in board)
            board0[r][c], board0[r0][c0] = board0[r0][c0], board0[r][c]
            return tuple(tuple(row) for row in board0)

        def neighbors(board):
            # Find the zero
            r, c = find_zero(board)
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0, board):
                    board0 = swap(r, c, r0, c0, board)
                    yield board0

        target = ((1,2,3), (4,5,0))
        visited = set()
        queue = collections.deque()
        board0 = tuple(tuple(row) for row in initial_board)
        queue.append((board0, 0))
        visited.add(board0)
        while queue:
            b, d = queue.popleft()
            if b == target:
                return d
            for b0 in neighbors(b):
                if b0 not in visited:
                    queue.append((b0, d + 1))
                    visited.add(b0)
        return -1


def test_1():
    board = [[1,2,3],[4,0,5]]
    expected = 1
    assert Solution().slidingPuzzle(board) == expected


def test_2():
    board = [[1,2,3],[5,4,0]]
    expected = -1
    assert Solution().slidingPuzzle(board) == expected