"""
LeetCode :: August 2022 Challenge :: Pacific Atlantic Water Flow
jramaswami
"""


import collections
from typing import *


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        def inbounds(r, c):
            return r >= 0 and r < len(matrix) and c >= 0 and c < len(matrix[r])

        def neighbors(r, c):
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                r0, c0 = r+dr, c+dc
                if inbounds(r0, c0):
                    yield r0, c0

        # Pacific
        queue = collections.deque()
        visited = [[False for _ in row] for row in matrix]
        pacific = [[False for _ in row] for row in matrix]
        for r, _ in enumerate(matrix):
            queue.append((r, 0))
            visited[r][0] = True
        for c, _ in enumerate(matrix[0][1:], start=1):
            queue.append((0, c))
            visited[0][c] = True
        while queue:
            r, c = queue.popleft()
            pacific[r][c] = True
            for r0, c0 in neighbors(r, c):
                # Would water travel down from r0, c0?
                if not visited[r0][c0] and matrix[r][c] <= matrix[r0][c0]:
                    queue.append((r0, c0))
                    visited[r0][c0] = True

        # Atlantic
        queue = collections.deque()
        visited = [[False for _ in row] for row in matrix]
        atlantic = [[False for _ in row] for row in matrix]
        for r, _ in enumerate(matrix):
            queue.append((r, len(matrix[r])-1))
            visited[r][len(matrix[r])-1] = True
        for c, _ in enumerate(matrix[0][:-1]):
            queue.append((len(matrix)-1, c))
            visited[len(matrix)-1][c] = True
        while queue:
            r, c = queue.popleft()
            atlantic[r][c] = True
            for r0, c0 in neighbors(r, c):
                # Would water travel down from r0, c0?
                if not visited[r0][c0] and matrix[r][c] <= matrix[r0][c0]:
                    queue.append((r0, c0))
                    visited[r0][c0] = True

        soln = []
        for r, row in enumerate(matrix):
            for c, _ in enumerate(row):
                if pacific[r][c] and atlantic[r][c]:
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


def test_3():
    "WA"
    matrix = [[2,1],[1,2]]
    expected = sorted([[0,0],[0,1],[1,0],[1,1]])
    result = sorted(Solution().pacificAtlantic(matrix))
    assert result == expected
