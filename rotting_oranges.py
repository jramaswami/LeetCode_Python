"""
LeetCode :: October 2021 Challenge :: 994. Rotting Oranges
jramaswami
"""


import enum


class Orange(enum.IntEnum):
    EMPTY = 0
    FRESH = 1
    ROTTEN = 2


class Solution:


    OFFSETS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


    def orangesRotting(self, grid: List[List[int]]) -> int:

        def inbounds(r, c):
            return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[r])

        def neighbors(r, c):
            for dr, dc in Solution.OFFSETS:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        fresh_oranges = 0
        queue = []
        for r, row in enumerate(grid):
            for c, orange in enumerate(row):
                if orange == Orange.FRESH:
                    fresh_oranges += 1
                elif orange == Orange.ROTTEN:
                    queue.append((r, c))

        ticks = 0
        new_queue = []
        while fresh_oranges and queue:
            ticks += 1
            for r, c in queue:
                for r0, c0 in neighbors(r, c):
                    orange = grid[r0][c0]
                    if orange == Orange.FRESH:
                        grid[r0][c0] = Orange.ROTTEN
                        fresh_oranges -= 1
                        new_queue.append((r0, c0))
            queue, new_queue = new_queue, []

        if fresh_oranges == 0:
            return ticks
        return -1
