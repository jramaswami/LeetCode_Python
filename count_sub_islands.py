"""
LeetCode
1905. Count Sub Islands
August 2024 Challenge
jramaswami
"""


import collections
import itertools
from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def inbounds(r, c):
            return r >= 0 and c >= 0 and r < len(grid1) and c < len(grid1[r])

        def neighbors(r, c):
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                r1, c1 = r + dr, c + dc
                if inbounds(r1, c1):
                    yield r1, c1

        # Establish island ids
        visited = [[False for _ in row] for row in grid1]
        island_id = [[-1 for _ in row] for row in grid1]
        island_id_generator = itertools.count(1)
        for r0, row in enumerate(grid1):
            for c0, val in enumerate(row):
                if not visited[r0][c0] and val == 1:
                    visited[r0][c0] = True
                    curr_island_id = next(island_id_generator)
                    queue = collections.deque()
                    queue.append((r0, c0))
                    while queue:
                        r1, c1 = queue.popleft()
                        island_id[r1][c1] = curr_island_id
                        for r2, c2 in neighbors(r1, c1):
                            if not visited[r2][c2] and grid1[r2][c2] == 1:
                                queue.append((r2, c2))
                                visited[r2][c2] = True

        # Check sub islands
        soln = 0
        visited = [[False for _ in row] for row in grid1]
        for r0, row in enumerate(grid1):
            for c0, val in enumerate(row):
                if not visited[r0][c0] and val == 1:
                    visited[r0][c0] = True
                    curr_island_id = island_id[r0][c0]
                    is_sub_island = True
                    queue.append((r0, c0))
                    while queue:
                        r1, c1 = queue.popleft()
                        if island_id[r1][c1] != curr_island_id:
                            is_sub_island = False
                        for r2, c2 in neighbors(r1, c1):
                            if not visited[r2][c2] and grid1[r2][c2] == 1:
                                queue.append((r2, c2))
                                visited[r2][c2] = True
                    if is_sub_island:
                        soln += 1
        return soln


def test_1():
    grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
    grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
    expected = 3
    assert Solution().countSubIslands(grid1, grid2) == expected


def test_2():
    grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
    grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
    expected = 2
    assert Solution().countSubIslands(grid1, grid2) == expected


def test_3():
    "WA"
    grid1 = [[1,1,1,1,0,0],[1,1,0,1,0,0],[1,0,0,1,1,1],[1,1,1,0,0,1],[1,1,1,1,1,0],[1,0,1,0,1,0],[0,1,1,1,0,1],[1,0,0,0,1,1],[1,0,0,0,1,0],[1,1,1,1,1,0]]
    grid2 = [[1,1,1,1,0,1],[0,0,1,0,1,0],[1,1,1,1,1,1],[0,1,1,1,1,1],[1,1,1,0,1,0],[0,1,1,1,1,1],[1,1,0,1,1,1],[1,0,0,1,0,1],[1,1,1,1,1,1],[1,0,0,1,0,0]]
    expected = 0
    assert Solution().countSubIslands(grid1, grid2) == expected