"""
LeetCode
3459. Length of Longest V-Shaped Diagonal Segment
August 2025 Challenge
jramaswami

REF: https://algo.monster/liteproblems/3459
"""


import functools
from typing import List


class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        next_digit = {1: 2, 2: 0, 0 : 2}

        def inbounds(r, c):
            return (0 <= r < len(grid)) and (0 <= c < len(grid[r]))

        @functools.cache
        def f(r, c, dr, dc, turned):
            result = 1
            successor = next_digit[grid[r][c]]
            if inbounds(r+dr, c+dc) and grid[r+dr][c+dc] == successor:
                result = 1 + f(r+dr, c+dc, dr, dc, turned)
            if not turned:
                dr0, dc0 = dc, -dr
                if inbounds(r+dr0, c+dc0) and grid[r+dr0][c+dc0] == successor:
                    result = max(result, 1 + f(r+dr0, c+dc0, dr0, dc0, True))
            return result

        directions = ((1,1), (-1,1), (1,-1), (-1,-1))
        soln = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 1:
                    for dr, dc in directions:
                        soln = max(soln, f(r, c, dr, dc, False))
        return soln
