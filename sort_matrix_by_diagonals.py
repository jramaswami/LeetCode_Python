"""
LeetCode
3446. Sort Matrix by Diagonals
August 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        def inbounds(r, c):
            return (0 <= r < len(grid)) and (0 <= c and c < len(grid[r]))

        def diagonal_generator(r, c):
            dr, dc = 1, 1
            while inbounds(r, c):
                yield r, c
                r, c = r + dr, c + dc

        # Bottom diagonals
        for init_r, _ in enumerate(grid):
            init_c = 0
            diagonal_values = []
            for r, c in diagonal_generator(init_r, init_c):
                diagonal_values.append(grid[r][c])
            diagonal_values.sort()
            print(f'{init_r=} {init_c=} {diagonal_values=}')
            for r, c in diagonal_generator(init_r, init_c):
                grid[r][c] = diagonal_values[-1]
                diagonal_values.pop()

        # Top diagonals
        for init_c, _ in enumerate(grid[0][1:], start = 1):
            init_r = 0
            diagonal_values = []
            for r, c in diagonal_generator(init_r, init_c):
                diagonal_values.append(grid[r][c])
            diagonal_values.sort(reverse=True)
            for r, c in diagonal_generator(init_r, init_c):
                grid[r][c] = diagonal_values[-1]
                diagonal_values.pop()
        
        return grid


def test_1():
    grid = [[1,7,3],[9,8,2],[4,5,6]]
    expected = [[8,2,3],[9,6,7],[4,5,1]]
    assert Solution().sortMatrix(grid) == expected
