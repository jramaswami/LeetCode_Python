"""
LeetCode
2658. Maximum Number of Fish in a Grid
January 2025 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def inbounds(r, c):
            return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[r])

        def neighbors(r, c):
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        visited = [[False for _ in row] for row in grid]
        def bfs(init_r, init_c):
            fish = 0
            queue = collections.deque()
            queue.append((init_r, init_c))
            visited[init_r][init_c] = True
            while queue:
                r, c = queue.popleft()
                fish += grid[r][c]
                for r0, c0 in neighbors(r, c):
                    if not visited[r0][c0] and grid[r0][c0] > 0:
                        visited[r0][c0] = True
                        queue.append((r0, c0))
            return fish

        soln = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val != 0:
                    soln = max(soln, bfs(r, c))
        return soln


def test_1():
    grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
    expected = 7
    assert Solution().findMaxFish(grid) == expected
