"""
LeetCode
2684. Maximum Number of Moves in a Grid
October 2024 Challenge
jramaswami
"""


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        offsets = ((-1, 1), (0, 1), (1, 1))
        dp = [[0 for _ in row] for row in grid]
        
        def inbounds(r, c):
            return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[r])
        
        def neighbors(r, c):
            for dr, dc in offsets:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0
        
        for c in range(len(grid[0]) - 2, -1, -1):
            for r in range(len(grid)):
                for r0, c0 in neighbors(r, c):
                    if grid[r][c] < grid[r0][c0]:
                        dp[r][c] = max(dp[r][c], dp[r0][c0] + 1)

        return max(row[0] for row in dp)
