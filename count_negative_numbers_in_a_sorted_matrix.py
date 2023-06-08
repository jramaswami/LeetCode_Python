"""
LeetCode
1351. Count Negative Numbers in a Sorted Matrix
June 2023 Challenge
jramaswami
"""


from typing import *


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total_numbers = len(grid) * len(grid[0])
        positive_numbers = 0
        row = 0
        col = len(grid[0]) - 1
        while row < len(grid) and col >= 0:
            if grid[row][col] < 0:
                col -= 1
            else:
                positive_numbers += (col + 1)
                row += 1
        return total_numbers - positive_numbers


def test_1():
    grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    expected = 8
    assert Solution().countNegatives(grid) == expected


def test_2():
    grid = [[3,2],[1,0]]
    expected = 0
    assert Solution().countNegatives(grid) == expected
