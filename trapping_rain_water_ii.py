"""
LeetCode
407. Trapping Rain Water II
January 2025 Challenge
jramaswami
"""


import collections
import heapq
from typing import List


QItem = collections.namedtuple('QItem', ['height', 'row', 'col'])

class Solution:
    def trapRainWater(self, height_map: List[List[int]]) -> int:
        def inbounds(r, c):
            return r >= 0 and c >= 0 and r < len(height_map) and c < len(height_map[r])

        def neighbors(r, c):
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0
        
        curr_height = 0
        # Add boundary elements
        visited = set()
        HEIGHT, WIDTH = len(height_map), len(height_map[0])
        for c in range(len(height_map[0])):
            visited.add((0, c))
            visited.add((HEIGHT-1, c))
        for r in range(1, HEIGHT-1):
            visited.add((r, 0))
            visited.add((r, WIDTH-1))
        queue = [QItem(height_map[r][c], r, c) for r, c in visited]
        heapq.heapify(queue)
        soln = max_height = 0
        while queue:
            item = heapq.heappop(queue)
            max_height = max(item.height, max_height)
            soln += (max_height - item.height)
            for r0, c0 in neighbors(item.row, item.col):
                if (r0, c0) not in visited:
                    visited.add((r0, c0))
                    item0 = QItem(height_map[r0][c0], r0, c0)
                    heapq.heappush(queue, item0)
        return soln


def test_1():
    height_map = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
    expected = 4
    assert Solution().trapRainWater(height_map) == expected


def test_2():
    height_map = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
    expected = 10
    assert Solution().trapRainWater(height_map) == expected


def test_3():
    "WA"
    height_map = [[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]] 
    expected = 14
    assert Solution().trapRainWater(height_map) == expected

