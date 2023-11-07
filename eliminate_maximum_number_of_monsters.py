"""
LeetCode
1921. Eliminate Maximum Number of Monsters
November 2023 Challenge
jramaswami
"""


import math
from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrival_time = [int(math.ceil(d / s)) for d, s in zip(dist, speed)]
        arrival_time.sort()
        soln = 0
        for t, a in enumerate(arrival_time):
            if t < a:
                soln += 1
            else:
                break
        return soln


def test_1():
    dist = [1,3,4]
    speed = [1,1,1]
    expected = 3
    assert Solution().eliminateMaximum(dist, speed) == expected


def test_2():
    dist = [1,1,2,3]
    speed = [1,1,1,1]
    expected = 1
    assert Solution().eliminateMaximum(dist, speed) == expected


def test_3():
    dist = [3,2,4]
    speed = [5,3,2]
    expected = 1
    assert Solution().eliminateMaximum(dist, speed) == expected