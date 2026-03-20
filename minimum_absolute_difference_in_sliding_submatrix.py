"""
LeetCode
3567. Minimum Absolute Difference in Sliding Submatrix
March 2026 Challenge
jramaswami
"""


from typing import List


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        soln = []
        for r, row in enumerate(grid):
            if r + k <= len(grid):
                soln.append([])
                for c, _ in enumerate(row):
                    if c + k <= len(row):
                        values = set()
                        for r1 in range(r, r+k):
                            for c1 in range(c, c+k):
                                values.add(grid[r1][c1])
                        values = list(sorted(values))
                        if len(values) == 1:
                            soln[-1].append(0)
                        else:
                            soln[-1].append(min(b - a for a, b in zip(values[:-1], values[1:])))
        return soln