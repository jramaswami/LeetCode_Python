"""
LeetCode
1895. Largest Magic Square
January 2026 Challenge
jramaswami
"""


import itertools
from typing import List


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        def is_magic_square(r, c, k):
            hsums = tuple(sum(grid[r+dr][c+dc] for dc in range(k)) for dr in range(k))
            vsums = tuple(sum(grid[r+dr][c+dc] for dr in range(k)) for dc in range(k))
            dsums = (
                sum(grid[r+d][c+d] for d in range(k)),
                sum(grid[r+k-1-d][c+d] for d in range(k))
            )
            t = hsums[0]
            return all(x == t for x  in itertools.chain(hsums, vsums, dsums))


        M = len(grid)
        N = len(grid[0])
        soln = 1
        for k in range(2, min(N, N)+1):
            for r, row in enumerate(grid):
                if k == soln:
                    break
                if r + k > len(grid):
                    break
                for c, _ in enumerate(row):
                    if c + k > len(row):
                        break
                    if is_magic_square(r, c, k):
                        soln = k
        return soln


def test_1():
    grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
    expected = 3
    assert Solution().largestMagicSquare(grid) == expected


def test_2():
    grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
    expected = 2
    assert Solution().largestMagicSquare(grid) == expected
