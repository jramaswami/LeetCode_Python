"""
LeetCode
3625. Count Number of Trapezoids II
December 2025 Challenge
jramaswami

REF: https://leetcode.doocs.org/en/lc/3625/#solution-1-hash-table-enumeration
"""


import collections
import math
from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # points by slope[slope][y-intercept]
        points_by_slope = collections.defaultdict(lambda: collections.defaultdict(int))
        # points by midpoint[midpoint][slope]
        points_by_midpoint = collections.defaultdict(lambda: collections.defaultdict(int))

        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points[i+1:], start=i+1):
                dx = x2 - x1
                dy = y2 - y1
                if dx == 0:
                    # Vertical line --> infinite slope
                    m = math.inf
                    # Y intercept = x1
                    b = x1
                else:
                    m = dy / dx
                    # Y intercept
                    b = (y1 * dx - x1 * dy) / dx

                points_by_slope[m][b] += 1

                # Shift midpoint to avoid negative numbers
                midp = (x1 + x2 + 2000) * 4000 + (y1 + y2 + 2000)
                points_by_midpoint[midp][m] += 1

        # Count trapezoids
        soln = 0
        for m in points_by_slope:
            s = 0
            for b in points_by_slope[m]:
                soln += s * points_by_slope[m][b]
                s += points_by_slope[m][b]
        # Subtract parellelograms to avoid double counting them
        for midp in points_by_midpoint:
            s = 0
            for m in points_by_midpoint[midp]:
                soln -= s * points_by_midpoint[midp][m]
                s += points_by_midpoint[midp][m]
        return soln