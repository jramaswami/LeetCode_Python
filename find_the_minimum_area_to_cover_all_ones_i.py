"""
LeetCode
3195. Find the Minimum Area to Cover All Ones I
August 2025 Challenge
jramaswami
"""


import math
from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        min_col = math.inf
        max_col = -math.inf
        min_row = math.inf
        max_row = -math.inf
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val:
                    min_col = min(min_col, c)
                    max_col = max(max_col, c)
                    min_row = min(min_row, r)
                    max_row = max(max_row, r)
        return (max_row - min_row + 1) * (max_col - min_col + 1)
