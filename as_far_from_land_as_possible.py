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

        dist = [[math.inf for _ in row] for row in grid]
        queue = collections.deque()
        soln = -1
        for r, row in enumerate(grid):
            for c, _ in enumerate(row):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    dist[r][c] = 0

        while queue:
            r, c = queue.popleft()
            for r0, c0 in neighbors(r, c):
                if dist[r][c] + 1 < dist[r0][c0]:
                    dist[r0][c0] = dist[r][c] + 1
                    queue.append((r0, c0))

        soln = -1
        for r, row in enumerate(grid):
            for c, _ in enumerate(row):
                if grid[r][c] == 0:
                    soln = max(soln, dist[r][c])
        return -1 if soln == math.inf else soln


def test_1():
    grid = [[1,0,1],[0,0,0],[1,0,1]]
    expected = 2
    assert Solution().maxDistance(grid) == expected


def test_2():
    grid = [[1,0,0],[0,0,0],[0,0,0]]
    expected = 4
    assert Solution().maxDistance(grid) == expected
