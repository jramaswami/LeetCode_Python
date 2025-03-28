"""
LeetCode
2503. Maximum Number of Points From Grid Queries
March 2025 Challenge
jramaswami
"""


from typing import List
import collections
import heapq


QItem = collections.namedtuple('QItem', ['value', 'row', 'col'])


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        def inbounds(r, c):
            return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[r])

        def neighbors(r, c):
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        queue = [QItem(grid[0][0], 0, 0)]
        queries0 = [(q, i) for i, q in enumerate(queries)]
        queries0.sort()
        visited = [[False for _ in row] for row in grid]
        visited[0][0] = True
        soln = [0 for _ in queries]
        curr = 0
        for q, i in queries0:
            while queue and queue[0].value < q:
                _, r, c = heapq.heappop(queue)
                curr += 1
                for r0, c0 in neighbors(r, c):
                    if not visited[r0][c0]:
                        visited[r0][c0] = True
                        heapq.heappush(queue, QItem(grid[r0][c0], r0, c0))
            soln[i] = curr
        return soln


def test_1():

    grid = [[1,2,3],[2,5,7],[3,5,1]]
    queries = [5,6,2]
    expected = [5,8,1]
    assert Solution().maxPoints(grid, queries) ==  expected
