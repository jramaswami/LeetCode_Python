"""
LeetCode :: December 2021 Challenge :: 56. Merge Intervals
jramaswami
"""


class Solution:

    def merge(self, intervals):
        intervals.sort()
        solns = []
        curr_left, curr_right = intervals[0]
        for left, right in intervals[1:]:
            if left > curr_right:
                solns.append([curr_left, curr_right])
                curr_left, curr_right = left, right
            else:
                curr_right = max(curr_right, right)
        solns.append([curr_left, curr_right])
        return solns


def test_1():
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    expected = [[1,6],[8,10],[15,18]]
    assert Solution().merge(intervals) == expected


def test_2():
    intervals = [[1,4],[4,5]]
    expected = [[1,5]]
    assert Solution().merge(intervals) == expected
