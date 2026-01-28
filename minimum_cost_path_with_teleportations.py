"""
LeetCode
3651. Minimum Cost Path with Teleportations
January 2026 Challenge
jramaswami

Thank you Larry!
"""


import math
import heapq
import collections
import sortedcontainers


class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        height = len(grid)
        width = len(grid[0])

        items = collections.defaultdict(list)
        ss = [sortedcontainers.SortedSet() for _ in range(k+1)]
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                items[val].append((r, c))
                for k in range(k+1):
                    ss[k].add(val)

        queue = []
        # dist[row][col][teleports]
        dist = [[[math.inf for _ in range(k+1)] for _ in row] for row in grid]
        dist[0][0][0] = 0
        heapq.heappush(queue, (0, 0, 0, 0))
        directions = ((0, 1), (1, 0))
        while queue:
            d, r, c, t = heapq.heappop(queue)
            if r == height - 1 and c == width - 1:
                return d
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < height and 0 <= nc < width:
                    nd = dist[r][c][t] + grid[nr][nc]
                    if dist[nr][nc][t] > nd:
                        dist[nr][nc][t] = nd
                        heapq.heappush(queue, (nd, nr, nc, t))
            if t + 1 <= k:
                while ss[t] and ss[t][0] <= grid[r][c]:
                    key = ss[t][0]
                    ss[t].remove(key)
                    for nr, nc in items[key]:
                        if dist[nr][nc][t+1] > dist[r][c][t]:
                            for mt in range(t+1, k+1):
                                dist[nr][nc][mt] = dist[r][c][t]
                            heapq.heappush(queue, (dist[r][c][t], nr, nc, t+1))


def test_1():
    grid = [[1,3,3],[2,5,4],[4,3,5]]
    k = 2
    expected = 7
    assert Solution().minCost(grid, k) == expected