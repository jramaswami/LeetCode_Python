"""
LeetCode
1568. Minimum Number of Days to Disconnect Island
August 2024 Challenge
jramaswami
"""


from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:

        def is_connected():
            # Determine connectedness, count the number of 1s, count degree of each cell
            components = 0
            visited = [[False for _ in row] for row in grid]

            def inbounds(r, c):
                return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[r])

            OFFSETS = ((0, 1), (0, -1), (1, 0), (-1, 0))
            def neighbors(r, c):
                for dr, dc in OFFSETS:
                    r0, c0 = r + dr, c + dc
                    if inbounds(r0, c0) and grid[r0][c0] == 1:
                        yield r0, c0

            def dfs(r, c):
                visited[r][c] = True
                for r0, c0 in neighbors(r, c):
                    if not visited[r0][c0]:
                        dfs(r0, c0)

            for r, row in enumerate(grid):
                for c, _ in enumerate(row):
                    if grid[r][c] == 1 and not visited[r][c]:
                        components += 1
                        dfs(r, c)

            return components == 1

        if not is_connected:
            return 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 1:
                    grid[r][c] = 0
                    if not is_connected():
                        return 1
                    grid[r][c] = 1
        return 2


def test_1():
    grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
    expected = 2
    assert Solution().minDays(grid) == expected


def test_2():
    grid = [[1,1]]
    expected = 2
    assert Solution().minDays(grid) == expected

def test_3():
    "WA"
    grid = [[1,1,0,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,0,1,1]]
    expected = 1
    assert Solution().minDays(grid) == expected


def test_4():
    "WA"
    grid = [[1,0,1,0]]
    expected = 0
    assert Solution().minDays(grid) == expected