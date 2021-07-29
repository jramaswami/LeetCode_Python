"""
LeetCode :: July 2021 Challenge :: 01 Matrix
jramaswami
"""


import collections
import math


class Solution:
    def updateMatrix(self, matrix):
        """
        Given an m x n binary matrix mat, return the distance of the nearest 0
        for each cell.
        """

        def inbounds(r, c):
            """Return True if (r, c) is inside matrix."""
            return r >= 0 and c >= 0 and r < len(matrix) and c < len(matrix[r])


        def neighbors(r, c):
            """Return neighbors of (r, c) (von Neumann neighborhood)."""
            offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in offsets:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield (r0, c0)


        dist = [[math.inf for _ in row] for row in matrix]
        Q = collections.deque()

        # Initialize distance and queue
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if val == 0:
                    Q.append((r, c))
                    dist[r][c] = 0

        # BFS to get shortest distances.
        while Q:
            r, c = Q.popleft()
            for r0, c0 in neighbors(r, c):
                # Only update and enqueue if we have shortened the distance.
                if 1 + dist[r][c] < dist[r0][c0]:
                    dist[r0][c0] = 1 + dist[r][c]
                    Q.append((r0, c0))

        return dist


def test_1():
    mat = [[0,0,0],[0,1,0],[0,0,0]]
    expected = [[0,0,0],[0,1,0],[0,0,0]]
    assert Solution().updateMatrix(mat) == expected


def test_2():
    mat = [[0,0,0],[0,1,0],[1,1,1]]
    expected = [[0,0,0],[0,1,0],[1,2,1]]
    assert Solution().updateMatrix(mat) == expected
