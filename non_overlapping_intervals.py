"""
LeetCode :: 435. Non-overlapping Intervals
jramaswami
"""


import math


class Solution:
    def eraseOverlapIntervals(self, intervals):
        # Corner case: empty intervals
        if intervals == []:
            return 0

        intervals.sort(key=lambda T: (T[1], T[0]))

        last_end = -math.inf
        interval_count = 0
        keepers = []
        for L, R in intervals:
            if L >= last_end:
                keepers.append((L, R))
                last_end = R
                interval_count += 1
        return len(intervals) - interval_count


def test_1():
    """WA"""
    intervals = [[1,2],[2,3],[3,4],[-100,-2],[5,7]]
    expected = 0
    assert Solution().eraseOverlapIntervals(intervals) == expected
