"""
LeetCode
959. Regions Cut By Slashes
August 2024 Challenge
jramaswami
"""


from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # Remove all lattice points connected to a slash
        removed_lattice_points = set()
        for cell_row, row in enumerate(grid):
            for cell_col, cell_val in enumerate(row):
                if cell_val == '/':
                    removed_lattice_points.add((cell_row+1, cell_col))
                    removed_lattice_points.add((cell_row, cell_col+1))
                elif cell_val == '\\':
                    removed_lattice_points.add((cell_row, cell_col))
                    removed_lattice_points.add((cell_row+1, cell_col+1))

        def inbounds(lr, lc):
            return lr >= 0 and lr <= len(grid) and lc >= 0 and lc <= len(grid[0])

        OFFSETS = ((0, 1), (0, -1), (1, 0), (-1, 0))
        def neighbors(lr, lc):
            for dlr, dlc in OFFSETS:
                lr0 = lr + dlr
                lc0 = lc + dlc
                if inbounds(lr0, lc0):
                    yield lr0, lc0

        components = 0
        visited = set()

        def visit(lr, lc):
            visited.add((lr, lc))
            for lr0, lc0 in neighbors(lr, lc):
                if (lr0, lc0) not in visited and (lr0, lc0) not in removed_lattice_points:
                    visit(lr0, lc0)

        for lattice_row in range(0, len(grid)+1):
            for lattice_col in range(0, len(grid[0])+1):
                if (lattice_row, lattice_col) not in visited and (lattice_row, lattice_col) not in removed_lattice_points:
                    components += 1
                    visit(lattice_row, lattice_col)
        return components


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