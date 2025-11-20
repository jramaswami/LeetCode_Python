"""
LeetCode
757. Set Intersection Size At Least Two
November 2025 Challenge
jramaswami

Thank You NeetCode.IO!
"""


from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        soln = 0
        intervals.sort(key=lambda t: (t[1], -t[0]))
        p1, p2 = -1, -1
        for left, right in intervals:
            if p2 < left:
                soln += 2
                p1, p2 = right-1, right
            elif p1 < left:
                soln += 1
                p1, p2 = p2, right
        return soln


def test_1():
    intervals = [[1,3],[3,7],[8,9]]
    expected = 5
    assert Solution().intersectionSizeTwo(intervals) == expected


def test_2():
    intervals = [[1,3],[1,4],[2,5],[3,5]]
    expected = 3
    assert Solution().intersectionSizeTwo(intervals) == expected


def test_3():
    intervals = [[1,2],[2,3],[2,4],[4,5]]
    expected = 5
    assert Solution().intersectionSizeTwo(intervals) == expected