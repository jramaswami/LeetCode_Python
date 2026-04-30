"""
LeetCode
3742. Maximum Path Score in a Grid
April 2026 Challenge
jramaswami
"""


from typing import List


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        cost = [0, 1, 1]
        # dp[cost][row][col] = score
        dp = [[[-1 for _ in row] for row in grid] for _ in range(k+1)]
        origin_cost = cost[grid[0][0]]
        origin_score = grid[0][0]
        dp[origin_cost][0][0] = origin_score
        for r, row in enumerate(grid):
            for c, _ in enumerate(row):
                for curr_cost in range(k+1):
                    curr_score = dp[curr_cost][r][c]
                    if curr_score < 0:
                        continue
                    # Right
                    if c + 1 < len(row):
                        next_cost = cost[grid[r][c+1]] + curr_cost
                        if next_cost <= k:
                            next_score = curr_score + grid[r][c+1]
                            dp[next_cost][r][c+1] = max(dp[next_cost][r][c+1], next_score)
                    # Down
                    if r + 1 < len(grid):
                        next_cost = cost[grid[r+1][c]] + curr_cost
                        if next_cost <= k:
                            next_score = curr_score + grid[r+1][c]
                            dp[next_cost][r+1][c] = max(dp[next_cost][r+1][c], next_score)
        return max(dp[cost][-1][-1] for cost in range(k+1))