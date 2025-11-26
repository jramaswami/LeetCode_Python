"""
LeetCode
2435. Paths in Matrix Whose Sum Is Divisible by K
November 2025 Challenge
jramaswami
"""


from typing import List
import collections


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = pow(10,9)+7
        grid = [[x % k for x in row] for row in grid]
        prev = [collections.defaultdict(int) for _ in grid[0]]
        curr = [collections.defaultdict(int) for _ in grid[0]]
        x = grid[0][0]
        curr[0][x] = 1

        for r, row in enumerate(grid):
            for c, x in enumerate(row):
                if r > 0:
                    for y in prev[c]:
                        z = (x + y) % k
                        curr[c][z] += prev[c][y]
                        curr[c][z] %= MOD
                if c > 0:
                    for y in curr[c-1]:
                        z = (x + y) % k
                        curr[c][z] += curr[c-1][y]
                        curr[c][z] %= MOD
            prev, curr = curr, [collections.defaultdict(int) for _ in grid[0]]

        soln = 0
        for key, val in prev[-1].items():
            if key % k == 0:
                soln += val
                soln %= MOD
        return soln