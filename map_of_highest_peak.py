"""
LeetCode
1765. Map of Highest Peak
January 2025 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def highestPeak(self, is_water: List[List[int]]) -> List[List[int]]:
        def inbounds(r, c):
            return r >= 0 and c >= 0 and r < len(is_water) and c < len(is_water[r])

        def neighbors(r, c):
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        soln = [[-1 for _ in row] for row in is_water]
        queue = collections.deque()
        for r, row in enumerate(is_water):
            for c, val in enumerate(row):
                if val == 1:
                    soln[r][c] = 0
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()
            h = soln[r][c]
            for r0, c0 in neighbors(r, c):
                if soln[r0][c0] == -1:
                    soln[r0][c0] = h + 1
                    queue.append((r0, c0))
        return soln


def test1():
    is_water = [[0,1],[0,0]]
    expected = [[1,0],[2,1]]
    assert Solution().highestPeak(is_water) == expected
        

def test2():
    is_water = [[0,0,1],[1,0,0],[0,0,0]] 
    expected = [[1,1,0],[0,1,1],[1,2,2]]
    assert Solution().highestPeak(is_water) == expected

