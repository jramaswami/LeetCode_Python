"""
LeetCode :: May 2022 Challenge :: Shortest Path in Binary Matrix
jramaswami
"""


import collections
import math


class Solution:

    # 8-neighborhood
    OFFSETS = [(0, 1), (0, -1), (-1, 0), (1, 0),
               (1, 1), (-1, 1), (1, -1), (-1, -1)]

    def shortestPathBinaryMatrix(self, grid):

        def inbounds(r, c):
            return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[r])

        def neighbors(r, c):
            for dr, dc in Solution.OFFSETS:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0) and grid[r0][c0] == 0:
                    yield r0, c0

        dist = [[math.inf for _ in row] for row in grid]
        queue = collections.deque()

        if grid[0][0] == 0:
            dist[0][0] = 1
            queue.append((0, 0))

        while queue:
            r, c = queue.popleft()
            for r0, c0 in neighbors(r, c):
                if dist[r][c] + 1 < dist[r0][c0]:
                    dist[r0][c0] = dist[r][c] + 1
                    queue.append((r0, c0))

        return (dist[-1][-1] if dist[-1][-1] < math.inf else -1)


def test_1():
    grid = [[0, 1], [1, 0]]
    assert Solution().shortestPathBinaryMatrix(grid) == 2


def test_2():
    grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    assert Solution().shortestPathBinaryMatrix(grid) == 4


def test_3():
    grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
    assert Solution().shortestPathBinaryMatrix(grid) == -1
