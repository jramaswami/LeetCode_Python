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
                if overlaps(x, insertedInterval):
                    # When we start overlapping, discard x and change state.
                    state = DURING
                    # Update interval to insert.
                    insertedInterval = merge(x, insertedInterval)
                elif insertedInterval[1] < x[0]:
                    # When we have cleared the inserted interval.
                    soln.append(insertedInterval)
                    soln.append(x)
                    state = AFTER
                else:
                    soln.append(x)
            elif state == DURING:
                if not overlaps(x, insertedInterval) or insertedInterval[1] < x[0]:
                    # When we stop overlapping or cleared inserted interval,
                    # insert interval, add x, and change state.
                    soln.append(insertedInterval)
                    soln.append(x)
                    state = AFTER
                else:
                    # Update interval to insert.
                    insertedInterval = merge(x, insertedInterval)
            else:
                soln.append(x)

        if state != AFTER:
            # If we haven't inserted interval yet, do so now.
            soln.append(insertedInterval)
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


def test_4():
    intervals = [[1,3],[6,9]]
    newInterval = [10,11]
    expected = [[1,3],[6,9], [10,11]]
    assert Solution().insert(intervals, newInterval) == expected


def test_5():
    intervals = [[1,3],[6,9]]
    newInterval = [0, 0]
    expected = [[0,0],[1,3],[6,9]]
    assert Solution().insert(intervals, newInterval) == expected


def test_6():
    intervals = [[1,3],[6,9]]
    newInterval = [2, 2]
    expected = [[1,3],[6,9]]
    assert Solution().insert(intervals, newInterval) == expected