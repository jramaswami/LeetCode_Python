"""
LeetCode
3643. Flip Square Submatrix Vertically
March 2026 Challenge
jramaswami
"""


class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        t, b = x, x + k - 1
        l, r = y, y + k
        while t < b:
            grid[t][l:r], grid[b][l:r] = grid[b][l:r], grid[t][l:r]
            t += 1
            b -= 1
        return grid