"""
Leet Code :: May 2021 Challenge :: Course Schedule III
jramaswami
"""
from typing import *
import heapq


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        queue = []
        total_time = 0
        for duration, expiration in sorted(courses, key=lambda t: t[1]):
            heapq.heappush(queue, (-duration, expiration))
            total_time += duration
            if total_time > expiration:
                delta, _ = heapq.heappop(queue)
                total_time += delta
        return len(queue)


def test_1():
    courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
    assert Solution().scheduleCourse(courses) == 3


def test_2():
    courses = [[1,2]]
    assert Solution().scheduleCourse(courses) == 1


def test_3():
    courses = [[3,2],[4,3]]
    assert Solution().scheduleCourse(courses) == 0


def test_4():
    courses = [[100,200],[400,1300],[1000,1250],[2000,3200]]
    assert Solution().scheduleCourse(courses) == 3
