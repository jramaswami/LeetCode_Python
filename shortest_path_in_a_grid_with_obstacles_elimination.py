"""
LeetCode :: September 2021 Challenge :: Shortest Path in a Grid with Obstacles Elimination
jramaswami
"""

import heapq
from math import inf
from collections import defaultdict


class Solution:

    def shortestPath(self, grid, k):

        def inbounds(r, c):
            """Return True if (r, c) is inside the grid."""
            return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0])

        def neighbors(r, c):
            """Return list of four neighbors."""
            offsets = ((1, 0), (-1, 0), (0, 1), (0, -1))
            for dr, dc in offsets:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        # Modified dijkstra
        Q = []
        heapq.heappush(Q, (0, grid[0][0], 0, 0))
        min_distance = defaultdict(lambda: inf)
        min_distance_and_removals = defaultdict(lambda: defaultdict(lambda: inf))
        min_distance[(0, 0)] = 0
        min_distance_and_removals[(0, 0)][grid[0][0]] = 0

        while Q:
            distance, removals, r, c = heapq.heappop(Q)

            # If this is farther than our best for bottom right, skip it.
            if distance > min_distance[(len(grid) - 1), (len(grid[0]) - 1)]:
                continue

            # If this isn't the smallest distance with the given number
            # of removals, skip this.
            if distance != min_distance_and_removals[(r, c)][removals]:
                continue

            for r0, c0 in neighbors(r, c):
                removals0 = removals + grid[r0][c0]
                # Do not go over the maximum number of removals
                if removals0 <= k:
                    distance0 = distance + 1
                    min_distance[(r0, c0)] = min(min_distance[(r0, c0)], distance0)
                    if distance0 < min_distance_and_removals[(r0, c0)][removals0]:
                        min_distance_and_removals[(r0, c0)][removals0] = distance0
                        heapq.heappush(Q, (distance0, removals0, r0, c0))


        soln = min_distance[(len(grid) - 1, len(grid[0]) - 1)]
        return -1 if soln == inf else soln


def test_1():
    grid = [[0,0,0], [1,1,0], [0,0,0], [0,1,1], [0,0,0]]
    k = 1
    expected = 6
    assert Solution().shortestPath(grid, k) == expected


def test_2():
    grid = [[0,1,1], [1,1,1], [1,0,0]]
    k = 1
    expected = -1
    assert Solution().shortestPath(grid, k) == expected
