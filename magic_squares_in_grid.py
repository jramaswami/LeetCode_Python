"""
LeetCode
840. Magic Squares In Grid
August 2024 Challenge
jramaswami
"""


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        def check_square(r0, c0):
            row_sums = [0, 0, 0]
            col_sums = [0, 0, 0]
            diagonal_sums = [0, 0]
            numbers = set()
            for dr in range(0, 3):
                for dc in range(0, 3):
                    r = r0 + dr
                    c = c0 + dc

                    if not (1 <= grid[r][c] <= 9):
                        return False
                    numbers.add(grid[r][c])
                    row_sums[dr] += grid[r][c]
                    col_sums[dc] += grid[r][c]
                    if dr == dc:
                        diagonal_sums[0] += grid[r][c]
                    if (dr, dc) in ((0, 2), (1, 1), (2, 0)):
                        diagonal_sums[1] += grid[r][c]
            return (
                len(numbers) == 9 and
                all(t == 15 for t in row_sums) and
                all(t == 15 for t in col_sums) and
                all (t == 15 for t in diagonal_sums)
            )

        soln = 0
        for r0 in range(0, len(grid) - 2):
            for c0 in range(0, len(grid[r0]) - 2):
                if check_square(r0, c0):
                    soln += 1
        return soln