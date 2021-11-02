"""
LeetCode :: November 2021 Challenge :: 980. Unique Paths III
jramaswami
"""


class Solver:
    START = 1
    END = 2
    EMPTY = 0
    OBSTACLE = -1
    OFFSETS = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def __init__(self, grid):
        self.grid = grid
        self.visited = [[False for _ in row] for row in grid]
        self.soln = 0
        self.visited_count = 0

        # Find the starting point and empty cells.
        self.empty_cells = 0
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == Solver.START:
                    self.start = (r, c)
                elif cell == Solver.EMPTY:
                    self.empty_cells += 1

    def _inbounds(self, r, c):
        return r >= 0 and c >= 0 and r < len(self.grid) and c < len(self.grid[r])

    def _neighbors(self, r, c):
        for dr, dc in Solver.OFFSETS:
            r0, c0 = r + dr, c + dc
            if self._inbounds(r0, c0):
                yield r0, c0

    def _dfs(self, r, c):
        self.visited[r][c] = True
        self.visited_count += 1
        if self.grid[r][c] == Solver.END:
            if self.visited_count == self.empty_cells + 2:
                self.soln += 1
        else:
            for r0, c0 in self._neighbors(r, c):
                if not self.visited[r0][c0] and self.grid[r0][c0] != Solver.OBSTACLE:
                    self._dfs(r0, c0)

        self.visited_count -= 1
        self.visited[r][c] = False

    def solve(self):
        self._dfs(*self.start)
        return self.soln

class Solution:
    def uniquePathsIII(self, grid):
        return Solver(grid).solve()


def test_1():
    grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    expected = 2
    assert Solution().uniquePathsIII(grid) == expected


def test_2():
    grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
    expected = 4
    assert Solution().uniquePathsIII(grid) == expected


def test_3():
    grid = [[0,1],[2,0]]
    expected = 0
    assert Solution().uniquePathsIII(grid) == expected