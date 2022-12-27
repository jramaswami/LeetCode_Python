"""
LeetCode
2279. Maximum Bags With Full Capacity of Rocks
December 2022 Challenge
jramaswami
"""


from typing import *


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        deltas = [c - r for c, r in zip(capacity, rocks)]
        deltas.sort()
        soln = 0
        for d in deltas:
            if d <= additionalRocks:
                additionalRocks -= d
                soln += 1
        return soln


def test_1():
    capacity = [2,3,4,5]
    rocks = [1,2,4,4]
    additionalRocks = 2
    expected = 3
    assert Solution().maximumBags(capacity, rocks, additionalRocks) == expected


def test_2():
    capacity = [10,2,2]
    rocks = [2,2,0]
    additionalRocks = 100
    expected = 3
    assert Solution().maximumBags(capacity, rocks, additionalRocks) == expected
