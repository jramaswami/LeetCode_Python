"""
LeetCode :: Shortest Path in Binary Matrix
jramaswami
"""
from typing import *
from math import inf
from collections import deque


def moore_neighborhood(row_index, col_index, grid):
    """Return list of neighbors in Moore (8) neighborhood."""
    neighbors = []
    offsets =[(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for row_off, col_off in offsets:
        row_index0 = row_index + row_off
        col_index0 = col_index + col_off
        if (col_index0 >= 0 and col_index0 < len(grid[0]) and row_index0 >= 0 and row_index0 < len(grid)):
            neighbors.append((row_index0, col_index0))
    return neighbors


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Corner case
        if grid[0][0] == 1:
            return -1

        # Distances
        dist = [[inf for _ in row] for row in grid]
        # Initialize the distances the first row at zero if the cell is open.
        dist[0][0] = 1
        # BFS from each starting point
        queue = deque()
        queue.append((0, 0))
        while queue:
            r, c = queue.popleft()
            for r0, c0 in moore_neighborhood(r, c, grid):
                if grid[r0][c0] == 0 and dist[r0][c0] > dist[r][c] + 1:
                    dist[r0][c0] = dist[r][c] + 1
                    queue.append((r0, c0))
        # Determine solution
        if dist[-1][-1] == inf:
            return -1
        else:
            return dist[-1][-1]
    

def test_1():
    grid = [[0,1],[1,0]]
    assert Solution().shortestPathBinaryMatrix(grid) == 2


def test_2():
    grid = [[0,0,0],[1,1,0],[1,1,0]]
    assert Solution().shortestPathBinaryMatrix(grid) == 4

def test_3():
    grid = [[1,0,0],[1,1,0],[1,1,0]]
    assert Solution().shortestPathBinaryMatrix(grid) == -1
