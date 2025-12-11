"""
LeetCode
3531. Count Covered Buildings
December 2025 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        by_x = collections.defaultdict(list)
        by_y = collections.defaultdict(list)
        for x, y in buildings:
            by_x[x].append(y)
            by_y[y].append(x)

        uncovered = set()
        for x in by_x:
            by_x[x].sort()
            # First and last in each list are uncovered
            y0, y1 = by_x[x][0], by_x[x][-1]
            uncovered.add((x, y0))
            uncovered.add((x, y1))
        for y in by_y:
            by_y[y].sort()
            # First and last in each list are uncovered
            x0, x1 = by_y[y][0], by_y[y][-1]
            uncovered.add((x0, y))
            uncovered.add((x1, y))

        return len(buildings) - len(uncovered)