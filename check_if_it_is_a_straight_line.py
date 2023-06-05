"""
LeetCode
1232. Check If It Is a Straight Line
June 2023 Challenge
jramaswami
"""


import fractions
from typing import *


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # Sort by y so we are always going up.
        coordinates.sort(key=lambda t: t[1])

        # Function to compute slope.
        def slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return fractions.Fraction(y2-y1, x2-x1)

        # Slope between first and last coordinates.
        m = slope(coordinates[0], coordinates[-1])

        # To be on the line, the points must have the same slope.
        return all(slope(p1, p2) == m for p1, p2 in zip(coordinates[:-1], coordinates[1:]))


def test_1():
    coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    expected = True
    assert Solution().checkStraightLine(coordinates) == expected


def test_2():
    coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
    expected = False
    assert Solution().checkStraightLine(coordinates) == expected


def test_3():
    "RTE"
    coordinates = [[0,0],[0,1],[0,-1]]
    expected = True
    assert Solution().checkStraightLine(coordinates) == expected