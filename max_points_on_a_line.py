"""
LeetCode
149. Max Points on a Line
January 2023 Challenge
jramaswami
"""


from typing import *
import collections
import math

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def compute_slope(p1, p2):
            if p2[0] == p1[0]:
                return math.inf
            return (p2[1] - p1[1]) / (p2[0] - p1[0])

        def same_slope(m1, m2):
            if m1 == math.inf or m2 == math.inf:
                return m1 == math.inf and m2 == math.inf
            return abs(m1 - m2) <= EPS

        EPS = pow(10, -5)
        points0 = sorted(tuple(p) for p in points)
        slopes = collections.defaultdict(list)
        soln = 0
        for i, p1 in enumerate(points0):
            for p2 in points0[i+1:]:
                m = compute_slope(p1, p2)
                collinear_points = 2
                for m0, k in slopes[p1]:
                    if same_slope(m, m0):
                        print('extending', m0, k)
                        collinear_points =  max(collinear_points, k+1)
                slopes[p2].append((m, collinear_points))
                soln = max(soln, collinear_points)
        return soln


def test_1():
    points = [[1,1],[2,2],[3,3]]
    expected = 3
    assert Solution().maxPoints(points) == expected


def test_2():
    points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    expected = 4
    assert Solution().maxPoints(points) == expected


def test_3():
    "WA"
    points = [[0,0]]
    expected = 1
    assert Solution().maxPoints(points) == expected