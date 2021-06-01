"""
LeetCode :: June 2021 Challenge :: Max Area of Island
jramaswami
"""


from typing import *
from collections import deque


def inbounds(row, col, grid):
    """Return True if (row, col) is inside grid."""
    return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])


def vn_neighborhood(row, col, grid):
    """Return the von Neumann neighborhood."""
    offsets = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for drow, dcol in offsets:
        row0, col0 = row + drow, col + dcol
        if inbounds(row0, col0, grid):
            yield (row0, col0)


def bfs(init_row, init_col, visited, grid):
    """BFS to determine the size of the island."""
    queue = deque()
    size = 0
    queue.append((init_row, init_col))
    visited.add((init_row, init_col))
    while queue:
        row, col = queue.popleft()
        size += 1
        for row0, col0 in vn_neighborhood(row, col, grid):
            if grid[row0][col0] and (row0, col0) not in visited:
                queue.append((row0, col0))
                visited.add((row0, col0))
    return size


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        soln = 0
        for r, row in enumerate(grid):
            for c, _ in enumerate(row):
                if grid[r][c] and (r, c) not in visited:
                    soln = max(soln, bfs(r, c, visited, grid))
        return soln



def test_1():
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], 
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], 
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    assert Solution().maxAreaOfIsland(grid) == 6


def test_2():
    grid = [[0,0,0,0,0,0,0,0]]
    assert Solution().maxAreaOfIsland(grid) == 0
