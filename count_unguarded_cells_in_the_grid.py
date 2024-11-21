"""
LeetCode
2257. Count Unguarded Cells in the Grid
November 2024 Challenge
jramaswami
"""


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        walls0 = set(tuple(x) for x in walls)
        guards0 = set(tuple(x) for x in guards)
        grid = [[1 for _ in range(n)] for _ in range(m)]

        def inbounds(r, c):
            return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[r])

        offsets = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        for r, c in walls:
            grid[r][c] = 0

        for guard in guards0:
            r, c = guard
            grid[r][c] = 0
            for dr, dc in offsets:
                r0, c0 = r + dr, c + dc
                while inbounds(r0, c0) and (r0, c0) not in guards0 and (r0, c0) not in walls0:
                    grid[r0][c0] = 0
                    r0, c0 = r0 + dr, c0 + dc

        return sum(sum(row) for row in grid)
