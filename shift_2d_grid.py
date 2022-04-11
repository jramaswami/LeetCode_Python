"""
LeetCode :: April 2022 Challenge :: 1260. Shift 2D Grid
jramaswami
"""


class Solution:

    def shiftGrid(self, grid, k):
        rows = len(grid)
        cols = len(grid[0])
        cells = rows * cols
        for _ in range(k):
            last = grid[-1][-1]
            for i in range(cells-1, 0, -1):
                r, c = divmod(i, cols)
                r0, c0 = divmod(i - 1, cols)
                grid[r][c] = grid[r0][c0]
            grid[0][0] = last
        return grid


def test_1():
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    k = 1
    expected = [[9,1,2],[3,4,5],[6,7,8]]
    assert Solution().shiftGrid(grid, k) == expected


def test_2():
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    k = 9
    expected = [[1,2,3],[4,5,6],[7,8,9]]
    assert Solution().shiftGrid(grid, k) == expected
