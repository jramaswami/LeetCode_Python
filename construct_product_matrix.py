"""
LeetCode
2906. Construct Product Matrix
March 2026 Challenge
jramaswami
"""


class Solution:
    def constructProductMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        R, C, MOD = len(grid), len(grid[0]), 12345
        P = [1 for _ in range(R * C)]
        i = 0
        curr = 1
        for r, row in enumerate(grid):
            for c, x in enumerate(row):
                P[i] *= curr
                P[i] %= MOD
                curr *= x
                curr %= MOD
                i += 1

        i = len(P) - 1
        curr = 1
        for r in range(R-1, -1, -1):
            for c in range(C-1, -1, -1):
                x = grid[r][c]
                P[i] *= curr
                P[i] %= MOD
                curr *= x
                i -= 1

        i = 0
        soln = []
        for r, row in enumerate(grid):
            soln.append([])
            for c, _ in enumerate(row):
                soln[-1].append(P[i] % MOD)
                i += 1
        return soln