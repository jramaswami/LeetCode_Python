"""
LeetCode
452. Minimum Number of Arrows to Burst Balloons
January 2023 Challenge
jramaswami
"""


import collections
import math


Event = collections.namedtuple('Event', ['x', 'type', 'index'])


START = -1
STOP = 1
WHITE = 0
GRAY = 1
BLACK = 2


class Solution:
    def findMinArrowShots(self, points):
        color = [WHITE for _ in points]
        events = []
        for i, (x1, x2) in enumerate(points):
            events.append(Event(x1, START, i))
            events.append(Event(x2, STOP, i))
        events.sort()

        soln = 0
        gray_balloons = []
        for event in events:
            print(gray_balloons, event)
            if event.type == STOP:
                assert color[event.index] != WHITE
                if color[event.index] == GRAY:
                    for b in gray_balloons:
                        color[b] = BLACK
                    gray_balloons = []
                    soln += 1
            else:
                gray_balloons.append(event.index)
                color[event.index] = GRAY
        if gray_balloons:
            soln += 1
        return soln


def test_1():
    points = [[10,16],[2,8],[1,6],[7,12]]
    expected = 2
    assert Solution().findMinArrowShots(points) == expected


def test_2():
    points = [[1,2],[3,4],[5,6],[7,8]]
    expected = 4
    assert Solution().findMinArrowShots(points) == expected


def test_3():
    points = [[1,2],[2,3],[3,4],[4,5]]
    expected = 2
    assert Solution().findMinArrowShots(points) == expected
