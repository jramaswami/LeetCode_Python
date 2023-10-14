"""
LeetCode
2742. Painting the Walls
October 2023 Challenge
jramaswami

Paid painter needs to paint only long enough for the volunteer painter to paint
the rest of the walls.
"""


import functools
import math
from typing import List


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:

        @functools.cache
        def rec(i, walls_to_paint):
            # Base case: all walls painted together
            if walls_to_paint <= 0:
                return 0

            # Base case: no more walls to choose from, but not all walls have
            # been painted.
            if i >= len(cost):
                return math.inf

            return min(
                # Paid painter can choose to paint this wall. If so, the
                # volunteer painter will paint one wall for each unit of time
                # the paid painter paints. The number of walls painted on this
                # step is 1 + time[i].
                cost[i] + rec(i+1, walls_to_paint - (1 + time[i])),
                # Paid painter can also choose to skip this wall.
                rec(i+1, walls_to_paint)
            )

        return rec(0, len(cost))


def test_1():
    cost = [1,2,3,2]
    time = [1,2,3,2]
    expected = 3
    assert Solution().paintWalls(cost, time) == expected


def test_2():
    cost = [2,3,4,2]
    time = [1,1,1,1]
    expected = 4
    assert Solution().paintWalls(cost, time) == expected