"""
LeetCode
2373. Largest Local Values in a Matrix
May 2024 Challenge
jramaswami
"""


import math
from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        soln = []
        for r, row in enumerate(grid[1:-1], start=1):
            soln.append([])
            for c, _ in enumerate(row[1:-1], start=1):
                max_val = -math.inf
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        max_val = max(max_val, grid[r+dr][c+dc])
                soln[-1].append(max_val)
        return soln


def test_1():
    grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
    expected = [[9,9],[8,6]]
    result = Solution().largestLocal(grid)
    assert expected == result


def test_2():
    grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    expected = [[2,2,2],[2,2,2],[2,2,2]]
    result = Solution().largestLocal(grid)
    assert expected == result