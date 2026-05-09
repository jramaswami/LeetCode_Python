"""
LeetCode
1914. Cyclically Rotating a Grid
May 2026 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def get_layer(top, bottom, left, right):
            layer = collections.deque()
            # top row
            for c in range(left, right+1):
                layer.append((top, c, grid[top][c]))
            # right side
            for r in range(top+1, bottom):
                layer.append((r, right, grid[r][right]))
            # bottom row
            for c in range(right, left-1, -1):
                layer.append((bottom, c, grid[bottom][c]))
            # left side
            for r in range(bottom-1, top, -1):
                layer.append((r, left, grid[r][left]))
            return layer

        def write_layer(top, bottom, left, right, layer, grid0):
            i = 0
            # top row
            for c in range(left, right+1):
                grid0[top][c] = layer[i][-1]
                i += 1
            # right side
            for r in range(top+1, bottom):
                grid0[r][right] = layer[i][-1]
                i += 1
            # bottom row
            for c in range(right, left-1, -1):
                grid0[bottom][c] = layer[i][-1]
                i += 1
            # left side
            for r in range(bottom-1, top, -1):
                grid0[r][left] = layer[i][-1]
                i += 1

        LEFT, RIGHT = 0, 1
        top = 0
        bottom = len(grid) - 1
        left = 0
        right = len(grid[0]) - 1
        i = 0
        soln = [[0 for _ in row] for row in grid]
        while top < bottom and left < right:
            layer = get_layer(top, bottom, left, right)
            layer.rotate(-k)
            write_layer(top, bottom, left, right, layer, soln)
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        return soln


def test_1():
    grid = [[40,10],[30,20]]
    k = 1
    expected = [[10,20],[40,30]]
    assert Solution().rotateGrid(grid, k) == expected

def test_2():
    grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    k = 2
    expected = [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
    assert Solution().rotateGrid(grid, k) == expected


def test_4():
    "WA"
    grid = [[10,1,4,8],[6,6,3,10],[7,4,7,10],[1,10,6,1],[2,1,1,10],[3,8,9,2],[7,1,10,10],[7,1,4,9],[2,2,4,2],[10,7,5,10]]
    k = 1
    expected = [[1,4,8,10],[10,3,7,10],[6,6,6,1],[7,4,1,10],[1,10,9,2],[2,1,10,10],[3,8,4,9],[7,1,4,2],[7,1,2,10],[2,10,7,5]]
    assert Solution().rotateGrid(grid, k) == expected