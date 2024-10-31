"""
LeetCode
2463. Minimum Total Distance Traveled
October 2024 Challenge
Thank You Larry!
"""


import functools
from typing import List


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        INF = pow(10, 20)

        @functools.cache
        def rec(r, f):
            if r >= len(robot):
                return 0

            if f >= len(factory):
                return INF

            # Do not take
            result = rec(r, f+1)
            # Take up to factory capacity of robots
            curr_dist = 0
            factory_position, factory_capacity = factory[f]
            for x in range(factory_capacity):
                if r+x >= len(robot):
                    break
                curr_dist += abs(robot[r+x] - factory_position)
                result = min(result, curr_dist + rec(r+x+1,f+1))
            return result

        return rec(0, 0)



def test_1():
    robot = [0,4,6]
    factory = [[2,2],[6,2]]
    expected = 4
    assert Solution().minimumTotalDistance(robot, factory) == expected


def test_2():
    robot = [1,-1]
    factory = [[-2,1],[2,1]]
    expected = 2
    assert Solution().minimumTotalDistance(robot, factory) == expected