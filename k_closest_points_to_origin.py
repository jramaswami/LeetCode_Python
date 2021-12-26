"""
LeetCode :: December 2021 Challenge :: 973. K Closest Points to Origin
jramaswami
"""


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points0 = sorted(points, key=lambda p: (p[0] * p[0]) + (p[1] * p[1]))
        return points0[:k]
