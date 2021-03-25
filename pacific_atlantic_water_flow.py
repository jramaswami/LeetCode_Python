"""
LeetCode :: March 2021 Challenge :: Pacific Atlantic Water Flow
jramaswami
"""
from typing import *
from collections import deque


def vn_neighborhood(row_index, col_index, matrix):
    """Return list of neighbors in von Neumann (4) neighborhood."""
    neighbors = []
    offsets =[(1, 0), (-1, 0), (0, 1), (0, -1)]
    for row_off, col_off in offsets:
        row_index0 = row_index + row_off
        col_index0 = col_index + col_off
        if (col_index0 >= 0 and col_index0 < len(matrix[0]) and row_index0 >= 0 and row_index0 < len(matrix)):
            neighbors.append((row_index0, col_index0))
    return neighbors


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []

        # Do the flow backwards, that is, for any given cell, ask from where
        # could water have flowed.  This means we reverse the comparison
        # operator from <= to >=.
        visited = [[False for _ in row] for row in matrix]
        pacific_flow = [[False for _ in row] for row in matrix]

        queue = deque()
        for c, _ in enumerate(matrix[0]):
            pacific_flow[0][c] = True
            visited[0][c] = True
            queue.append((0, c))
        for r, _ in enumerate(matrix):
            pacific_flow[r][0] = True
            visited[r][0] = True
            queue.append((r, 0))

        while queue:
            r, c = queue.popleft()
            for r0, c0 in vn_neighborhood(r, c, matrix):
                if matrix[r0][c0] >= matrix[r][c] and not visited[r0][c0]:
                    pacific_flow[r0][c0] = True
                    visited[r0][c0] = True
                    queue.append((r0, c0))

        visited = [[False for _ in row] for row in matrix]
        atlantic_flow = [[False for _ in row] for row in matrix]

        queue = deque()
        N = len(matrix)
        for c, _ in enumerate(matrix[0]):
            atlantic_flow[N-1][c] = True
            visited[N-1][c] = True
            queue.append((N-1, c))
        M = len(matrix[0])
        for r, _ in enumerate(matrix):
            atlantic_flow[r][M-1] = True
            visited[r][M-1] = True
            queue.append((r, M-1))

        while queue:
            r, c = queue.popleft()
            for r0, c0 in vn_neighborhood(r, c, matrix):
                if matrix[r0][c0] >= matrix[r][c] and not visited[r0][c0]:
                    atlantic_flow[r0][c0] = True
                    visited[r0][c0] = True
                    queue.append((r0, c0))

        # See where both can flow.
        soln = []
        for r, row in enumerate(matrix):
            for c, _ in enumerate(row):
                if pacific_flow[r][c] and atlantic_flow[r][c]:
                    soln.append([r, c])
        return soln


def test_1():
    matrix = [[1, 2, 2, 3, 5],
               [3, 2, 3, 4, 4],
               [2, 4, 5, 3, 1],
               [6, 7, 1, 4, 5],
               [5, 1, 1, 2, 4]]
    expected = sorted([[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]])
    result = sorted(Solution().pacificAtlantic(matrix))
    assert result == expected

def test_2():
    """Runtime error."""
    matrix = [[3,3,3,3,3,3],[3,0,3,3,0,3],[3,3,3,3,3,3]]
    expected = sorted( [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[1,0],[1,2],[1,3],[1,5],[2,0],[2,1],[2,2],[2,3],[2,4],[2,5]])
    result = sorted(Solution().pacificAtlantic(matrix))
    assert result == expected
