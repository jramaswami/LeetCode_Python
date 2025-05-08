"""
LeetCode
3342. Find Minimum Time to Reach Last Room II
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

        heap = [(0, 0, 0, 0)]
        INF = pow(10, 10)
        # dist[move parity][row][column]
        dist = [[[INF for _ in row] for row in moveTime] for _ in range(2)]
        dist[0][0][0] = 0
        while heap:
            curr_dist, parity, r, c = heapq.heappop(heap)
            if curr_dist != dist[parity][r][c]:
                continue
            if r == len(moveTime) - 1 and c == len(moveTime[r]) - 1:
                return curr_dist
            for r0, c0 in neighbors(r, c):
                next_dist = max(curr_dist, moveTime[r0][c0]) + 1
                if parity:
                    next_dist += 1
                next_parity = (parity + 1) % 2
                if next_dist < dist[next_parity][r0][c0]:
                    dist[next_parity][r0][c0] = next_dist
                    heapq.heappush(heap, (next_dist, next_parity, r0, c0))


def test_1():
    moveTime = [[0,4],[4,4]]
    expected = 7
    assert Solution().minTimeToReach(moveTime) == expected


def test_2():
    moveTime = [[0,0,0,0],[0,0,0,0]]
    expected = 6
    assert Solution().minTimeToReach(moveTime) == expected


def test_3():
    moveTime = [[0,1],[1,2]]
    expected = 4

    assert Solution().minTimeToReach(moveTime) == expected
