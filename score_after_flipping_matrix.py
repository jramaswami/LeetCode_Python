"""
LeetCode
861. Score After Flipping Matrix
May 2024 Challenge
jramaswami
"""


from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        def flip(x):
            if x == 1:
                return 0
            return 1

        def row_to_num(row):
            n = 0
            for x in row:
                n = n << 1
                n = n + x
            return n

        # Flip any row with leading zeros
        for r, row in enumerate(grid):
            if row[0] == 0:
                grid[r] = [flip(x) for x in row]

        # Flip any col with more than half zeros
        # except first column
        for c, _ in enumerate(grid[0][1:], start=1):
            ones = sum(row[c] for row in grid)
            if ones < len(grid) / 2:
                for r, _ in enumerate(grid):
                    grid[r][c] = flip(grid[r][c])

        return sum(row_to_num(r) for r in grid)


def test_1():
    grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
    expected = 39
    result = Solution().matrixScore(grid)
    assert result == expected


def test_2():
    grid = [[0]]
    expected = 1
    result = Solution().matrixScore(grid)
    assert result == expected