"""
LeetCode
1219. Path with Maximum Gold
May 2024 Challenge
jramaswmai
"""


import collections
from typing import List


Posn = collections.namedtuple('Posn', ['row', 'col'])


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        OFFSETS = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def inbounds(u):
            return (
                u.row >= 0 and
                u.col >= 0 and
                u.row < len(grid) and
                u.col < len(grid[u.row])
            )

        def neighbors(u):
            for dr, dc in OFFSETS:
                v = Posn(u.row + dr, u.col + dc)
                if inbounds(v):
                    yield v

        def dfs(u):
            if grid[u.row][u.col] == 0:
                return 0

            x = grid[u.row][u.col]
            grid[u.row][u.col] = 0
            result = 0
            for v in neighbors(u):
                result = max(result, x + dfs(v))
            grid[u.row][u.col] = x
            return result


        soln = 0
        for r, row in enumerate(grid):
            for c, _ in enumerate(row):
                soln = max(soln, dfs(Posn(r, c)))
        return soln


def test_1():
    grid = [[0,6,0],[5,8,7],[0,9,0]]
    expected = 24
    result = Solution().getMaximumGold(grid)
    assert result == expected


def test_2():
    grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
    expected = 28
    result = Solution().getMaximumGold(grid)
    assert result == expected
