"""
LeetCode
980. Unique Paths III
December 2022 Challenge
jramaswami
"""


class Solution:
    def uniquePathsIII(self, grid):
        START = 1
        TARGET = 2
        OBSTACLE = -1
        OFFSETS = ((0, 1), (0, -1), (1, 0), (-1, 0))
        visited = [[False for _ in row] for row in grid]

        def inbounds(r, c):
            "Return True if (r, c) is inbounds."
            return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[r])

        def neighbors(r, c):
            "Return the 4-neighbors of (r, c)."
            for dr, dc in OFFSETS:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        def dfs(r, c, k, empty_cells):
            "DFS to count number of was to reach target cell."
            result = 0

            if grid[r][c] == TARGET:
                if k == empty_cells:
                    result = 1
            else:
                result = 0
                visited[r][c] = True
                for r0, c0 in neighbors(r, c):
                    if not visited[r0][c0] and grid[r0][c0] != OBSTACLE:
                        result += dfs(r0, c0, k+1, empty_cells)
                visited[r][c] = False

            return result

        init_r = init_c = -1
        empty_cells = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == START:
                    init_r, init_c = r, c
                if val != OBSTACLE:
                    empty_cells += 1

        return dfs(init_r, init_c, 1, empty_cells)


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
