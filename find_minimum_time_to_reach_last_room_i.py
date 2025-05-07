"""
LeetCode
3341. Find Minimum Time to Reach Last Room I
May 2025 Challenge
jramaswami
"""


import heapq
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        def inbounds(r, c):
            return r >= 0 and c >= 0 and r < len(moveTime) and c < len(moveTime[r])

        def neighbors(r, c):
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        heap = [(0, 0, 0)]
        INF = pow(10, 10)
        dist = [[INF for _ in row] for row in moveTime]
        dist[0][0] = 0
        while heap:
            curr_dist, r, c = heapq.heappop(heap)
            if curr_dist != dist[r][c]:
                continue
            if r == len(moveTime) - 1 and c == len(moveTime[r]) - 1:
                return curr_dist
            for r0, c0 in neighbors(r, c):
                next_dist = max(curr_dist, moveTime[r0][c0]) + 1
                if next_dist < dist[r0][c0]:
                    dist[r0][c0] = next_dist
                    heapq.heappush(heap, (next_dist, r0, c0))


def test_1():
    moveTime = [[0,4],[4,4]]
    expected = 6
    assert Solution().minTimeToReach(moveTime) == expected


def test_2():
    moveTime = [[0,0,0],[0,0,0]]
    expected = 3
    assert Solution().minTimeToReach(moveTime) == expected


def test_4():
    "WA"
    moveTime = [[56,93],[3,38]]
    expected = 39
    assert Solution().minTimeToReach(moveTime) == expected
