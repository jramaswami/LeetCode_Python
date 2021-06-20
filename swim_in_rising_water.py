"""
LeetCode :: June 2021 Challenge :: Swim in Rising Water
jramaswami
"""


import heapq
from collections import deque
from math import inf


class Solution:
    def swimInWater(self, grid):

        def inbounds(r, c):
            """Return True if r, c is inside the grid."""
            return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0])

        def neighbors(r, c):
            """Return the neighbors of r, c."""
            offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in offsets:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield (r0, c0)

        high_water = [[inf for val in row] for row in grid]
        high_water[0][0] = grid[0][0]
        queue = [(grid[0][0], 0, 0)]
        while queue:
            hw, r, c = heapq.heappop(queue)
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return hw
            for r0, c0 in neighbors(r, c):
                hw0 = max(hw, grid[r0][c0])
                if high_water[r0][c0] > hw0:
                    heapq.heappush(queue, (hw0, r0, c0))
                    high_water[r0][c0] = hw0


def test_1():
    grid = [[0,2],[1,3]]
    expected = 3
    assert Solution().swimInWater(grid) == expected


def test_2():
    grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
    expected = 16
    assert Solution().swimInWater(grid) == expected


def test_3():
    """WA"""
    grid = [[10,12,4,6],[9,11,3,5],[1,7,13,8],[2,0,15,14]]
    expected = 14
    assert Solution().swimInWater(grid) == expected