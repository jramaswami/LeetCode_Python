"""
LeetCode :: April 2022 Challenge :: 1631. Path With Minimum Effort
jramaswami
"""


import heapq
import math


class Solution:

    OFFSETS = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def minimumEffortPath(self, heights):

        def inbounds(r, c):
            return (
                r >= 0 and r < len(heights) and
                c >= 0 and c < len(heights[r])
            )

        def neighbors(r, c):
            for dr, dc in Solution.OFFSETS:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        dist = [[math.inf for _ in row] for row in heights]
        dist[0][0] = 0
        Q = [(0, 0, 0)]
        while Q:
            d, r, c = heapq.heappop(Q)
            if r == len(heights) - 1 and c == len(heights[r]) - 1:
                return d

            for r0, c0 in neighbors(r, c):
                d0 = max(d, abs(heights[r][c] - heights[r0][c0]))
                if d0 < dist[r0][c0]:
                    heapq.heappush(Q, (d0, r0, c0))
                    dist[r0][c0] = d0


def test_1():
    heights = [[1,2,2],[3,8,2],[5,3,5]]
    expected = 2
    assert Solution().minimumEffortPath(heights) == expected


def test_2():
    heights = [[1,2,3],[3,8,4],[5,3,5]]
    expected = 1
    assert Solution().minimumEffortPath(heights) == expected


def test_3():
    heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
    expected = 0
    assert Solution().minimumEffortPath(heights) == expected


def test_4():
    "WA"
    heights = [[1,10,6,7,9,10,4,9]]
    expected = 9
    assert Solution().minimumEffortPath(heights) == expected

