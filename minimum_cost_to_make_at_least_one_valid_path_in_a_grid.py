"""
LeetCode
1368. Minimum Cost to Make at Least One Valid Path in a Grid
January 2025 Challenge
jramaswami
"""


import collections
import math
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        dirns = (None, (0, 1), (0, -1), (1, 0), (-1, 0))

        def inbounds(r, c):
            return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[r])

        def neighbors(r, c):
            for dr, dc in dirns[1:]:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        dist = [[math.inf for _ in row] for row in grid]
        dist[0][0] = 0
        queue = collections.deque()
        queue.append((0, 0))

        while queue:
            r, c = queue.popleft()
            dr, dc = dirns[grid[r][c]]
            r0, c0 = r + dr, c + dc
            if inbounds(r0, c0) and dist[r][c] < dist[r0][c0]:
                dist[r0][c0] = dist[r][c]
                queue.append((r0, c0))
            for r0, c0 in neighbors(r, c):
                if dist[r][c] + 1 < dist[r0][c0]:
                    dist[r0][c0] = dist[r][c] + 1
                    queue.append((r0, c0))
        return dist[-1][-1]


def test_1():
    grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
    expected = 3
    assert Solution().minCost(grid) == expected


def test_2():
    grid = [[1,1,3],[3,2,2],[1,1,4]]
    expected = 0
    assert Solution().minCost(grid) == expected
        

def test_3():
    grid = [[1,2],[4,3]]
    expected = 1
    assert Solution().minCost(grid) == expected
