"""
LeetCode
1266. Minimum Time Visiting All Points
December 2023 Challenge
jramaswami
"""


from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        soln = 0
        for a, b in zip(points[:-1], points[1:]):
            dx = abs(a[0] - b[0])
            dy = abs(a[1] - b[1])
            soln += max(dx, dy)
        return soln