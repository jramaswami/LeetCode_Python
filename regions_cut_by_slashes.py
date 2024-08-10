"""
LeetCode
959. Regions Cut By Slashes
August 2024 Challenge
jramaswami
"""


from typing import List
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        original_rows, original_cols = len(grid), len(grid[0])
        scaled_rows, scaled_cols = 3 * original_rows, 3 * original_cols
        scaled_grid = [[0 for _ in range(scaled_cols)] for _ in range(scaled_rows)]

        for r in range(original_rows):
            for c in range(original_cols):
                r0, c0 = 3 * r, 3 * c
                if grid[r][c] == '/':
                    scaled_grid[r0][c0+2] = 1
                    scaled_grid[r0+1][c0+1] = 1
                    scaled_grid[r0+2][c0] = 1
                elif grid[r][c] == '\\':
                    scaled_grid[r0][c0] = 1
                    scaled_grid[r0+1][c0+1] = 1
                    scaled_grid[r0+2][c0+2] = 1

        def inbounds(r, c):
            return (
                r >= 0 and r < len(scaled_grid) and
                c >= 0 and c < len(scaled_grid[r])
            )

        visited = set()
        OFFSETS = ((0, 1), (0, -1), (1, 0), (-1, 0))
        def dfs(r, c):
            visited.add((r, c))
            for dr, dc in OFFSETS:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0) and scaled_grid[r0][c0] == 0 and (r0, c0) not in visited:
                    dfs(r0, c0)

        soln = 0
        for r in range(scaled_rows):
            for c in range(scaled_cols):
                if scaled_grid[r][c] == 0 and (r, c) not in visited:
                    soln += 1
                    dfs(r, c)
        return soln


def test_1():
    grid = [" /", "/ "]
    expected = 2
    assert Solution().regionsBySlashes(grid) == expected


def test_2():
    grid = [" /", "  "]
    expected = 1
    assert Solution().regionsBySlashes(grid) == expected


def test_3():
    grid = ["/\\", "\\/"]
    expected = 5
    assert Solution().regionsBySlashes(grid) == expected


def test_4():
    "WA"
    grid = ["//", "/ "]
    expected = 3
    assert Solution().regionsBySlashes(grid) == expected