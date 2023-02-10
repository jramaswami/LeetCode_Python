"""
LeetCode
1162. As Far from Land as Possible
February 2023 Challenge
jramaswami
"""


import collections
import math
from typing import *


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        def inbounds(r, c):
            return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[r])

        def neighbors(r, c):
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        def bfs(init_r, init_c):
            visited = [[False for _ in row] for row in grid]
            visited[init_r][init_c] = True
            queue = [(init_r, init_c)]
            new_queue = []
            dist = -1
            while queue:
                dist += 1
                for r, c in queue:
                    if grid[r][c] == 1:
                        return dist
                    for r0, c0 in neighbors(r, c):
                        if not visited[r0][c0]:
                            new_queue.append((r0, c0))
                            visited[r0][c0] = True
                queue, new_queue = new_queue, []
            return -1

        soln = -1
        for r, row in enumerate(grid):
            for c, _ in enumerate(row):
                if grid[r][c] == 0:
                    soln = max(soln, bfs(r, c))
        return soln


def test_1():
    grid = [[1,0,1],[0,0,0],[1,0,1]]
    expected = 2
    assert Solution().maxDistance(grid) == expected


def test_2():
    grid = [[1,0,0],[0,0,0],[0,0,0]]
    expected = 4
    assert Solution().maxDistance(grid) == expected
