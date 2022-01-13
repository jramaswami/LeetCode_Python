"""
LeetCode :: January 2022 Challenge :: 452. Minimum Number of Arrows to Burst Balloons
jramaswami
"""


import collections
import enum


class EType(enum.IntEnum):
    START = -1
    STOP = 1


Event = collections.namedtuple('Event', ['x', 'type', 'index'])


class Solution:
    def findMinArrowShots(self, points):
        events = []
        for i, (a, b) in enumerate(points):
            events.append(Event(a, EType.START, i))
            events.append(Event(b, EType.STOP, i))
        events.sort()

        soln = 0
        curr_balloons = set()
        for e in events:
            if e.type == EType.START:
                curr_balloons.add(e.index)
            else:
                if e.index in curr_balloons:
                    # We are going to remove a balloon.  This is the max for
                    # this interval of xs.
                    soln += 1
                    curr_balloons.clear()
                else:
                    # We have already shot this balloon so we can ignore it
                    # passing out of range.
                    pass
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
