"""
LeetCode
57. Insert Interval
January 2023 Challenge
jramaswami
"""


from typing import *


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        BEFORE, DURING, AFTER = 1, 2, 3

        def overlaps(x, y):
            "Return True if intervals overlap."
            return x[0] <= y[1] and x[1] >= y[0]

        def merge(x, y):
            "Merge intervals."
            return [min(x[0], y[0]), max(x[1], y[1])]

        soln = []
        state = BEFORE
        insertedInterval = newInterval
        for x in intervals:
            if state == BEFORE:
                if overlaps(x, newInterval):
                    # When we start overlapping, discard x and change state.
                    state = DURING
                    # Update interval to insert.
                    insertedInterval = merge(x, insertedInterval)
                else:
                    soln.append(x)
            elif state == DURING:
                if not overlaps(x, newInterval):
                    # When we stop overlapping, insert interval,
                    # add x and change state.
                    soln.append(insertedInterval)
                    soln.append(x)
                    state == AFTER
                else:
                    # Update interval to insert.
                    insertedInterval = merge(x, insertedInterval)
            else:
                soln.append(x)

        return soln


def test_1():
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    expected = [[1,5],[6,9]]
    assert Solution().insert(intervals, newInterval) == expected


def test_2():
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    expected = [[1,2],[3,10],[12,16]]
    assert Solution().insert(intervals, newInterval) == expected


def test_3():
    "WA"
    intervals = []
    newInterval = [4,8]
    expected = [[4,8]]
    assert Solution().insert(intervals, newInterval) == expected