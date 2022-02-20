"""
LeetCode :: February 2022 Challenge :: 1288. Remove Covered Intervals
jramaswami
"""


class Solution:

    def removeCoveredIntervals(self, intervals):
        START = -1
        STOP = 1
        events = []
        for i, (start, stop) in enumerate(intervals):
            events.append((start, START, stop, i))
            events.append((stop, STOP, -start, i))
        events.sort()

        active = set()
        covered = [0 for _ in intervals]
        for time, etype, _, i in events:
            if etype == START:
                active.add(i)
            elif etype == STOP:
                active.remove(i)
                a, b = intervals[i]
                for j in active:
                    c, d = intervals[j]
                    if c <= a and b <= d:
                        covered[i] = 1
                        break

        return len(covered) - sum(covered)


def test_1():
    intervals = [[1,4],[3,6],[2,8]]
    expected = 2
    assert Solution().removeCoveredIntervals(intervals) == expected


def test_2():
    intervals = [[1,4],[2,3]]
    expected = 1
    assert Solution().removeCoveredIntervals(intervals) == expected


def test_3():
    "WA"
    intervals = [[3,10],[4,10],[5,11]]
    expected = 2
    assert Solution().removeCoveredIntervals(intervals) == expected
