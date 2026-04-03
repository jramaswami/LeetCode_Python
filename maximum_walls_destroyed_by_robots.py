"""
LeetCode
3661. Maximum Walls Destroyed by Robots
April 2026 Challenge
jramaswami
"""


from typing import List
import bisect


class Robot:
    def __init__(self, index, distance):
        self.index = index
        self.distance = distance
        self.left_limit = index - distance
        self.right_limit = index + distance

    def __repr__(self):
        return f'Robot(left={self.left_limit}, index={self.index}, right={self.right_limit})'


class Solution:
    def maxWalls(self, robots0: List[int], distance0: List[int], walls0: List[int]) -> int:
        robots = [Robot(i, d) for i, d in zip(robots0, distance0)]
        robots.sort(key=lambda r: r.index)
        walls = list(sorted(walls0))
        # print(f'{walls=}')
        # dp_left[i] by robot[i] if it shoots left
        dp_left = [0 for _ in robots]
        # dp_right[i] by robot[i] if it shoots right
        dp_right = [0 for _ in robots]

        for i, robot in enumerate(robots):
            # print(f'{i=} {robot=}')
            # I am shooting left
            # Previous robot shot left
            left_limit = robot.left_limit
            # My bullet cannot pass the previous robot
            if i - 1 >= 0:
                left_limit = max(left_limit, robots[i-1].index + 1)
            # Index of the leftmost wall I can shoot (gte left limit)
            left_index = bisect.bisect_left(walls, left_limit)
            # Index of the rightmost wall to my left (lte my index)
            right_index = bisect.bisect_right(walls, robot.index) - 1
            # Number of walls I can hit
            curr_robot_destroyed = right_index - left_index + 1
            prev_robot_destroyed = dp_left[i-1] if i-1 >= 0 else 0
            # print(f'L L {left_limit=} {left_index=} {right_index=} {prev_robot_destroyed=} {curr_robot_destroyed=}')
            dp_left[i] = max(dp_left[i], prev_robot_destroyed + curr_robot_destroyed)

            # I am shooting left
            # Previous robot shot right
            left_limit = robot.left_limit
            # My bullet cannot pass the bullet shot by previous robot
            if i - 1 >= 0:
                left_limit = max(left_limit, robots[i-1].right_limit + 1)
            # Index of the leftmost wall I can shoot (gte left limit)
            left_index = bisect.bisect_left(walls, left_limit)
            # Index of the rightmost wall to my left (lte my index)
            right_index = bisect.bisect_right(walls, robot.index) - 1
            # Number of walls I can hit
            curr_robot_destroyed = right_index - left_index + 1
            prev_robot_destroyed = dp_left[i-1] if i-1 > 0 else 0
            dp_left[i] = max(dp_left[i], prev_robot_destroyed + curr_robot_destroyed)

            # I am shooting right
            # Previous robot's shot does not change anything
            right_limit = robot.right_limit
            # My bullet cannot pass next robot
            if i + 1 < len(robots):
                right_limit = min(right_limit, robots[i+1].index - 1)
            # Index of rightmost wall I can shoot (lte right limit)
            right_index = bisect.bisect_right(walls, right_limit) - 1
            # Index of leftmost wall to my right (gte my index)
            left_index = bisect.bisect_left(walls, robot.index)
            curr_robot_destroyed = right_index - left_index + 1
            prev_robot_destroyed = 0
            if i - 1 >= 0:
                prev_robot_destroyed = max(dp_left[i-1], dp_right[i-1])
            dp_right[i] = max(dp_right[i], prev_robot_destroyed + curr_robot_destroyed)

        # print(dp_left)
        # print(dp_right)
        return max(dp_left[-1], dp_right[-1])



def test_1():
    robots = [4]
    distance = [3]
    walls = [1,10]
    expected = 1
    assert Solution().maxWalls(robots, distance, walls) == expected


def test_2():
    robots = [10,2]
    distance = [5,1]
    walls = [5,2,7]
    expected = 3
    assert Solution().maxWalls(robots, distance, walls) == expected


def test_3():
    robots = [1,2]
    distance = [100,1]
    walls = [10]
    expected = 0
    assert Solution().maxWalls(robots, distance, walls) == expected


def test_530():
    "WA"
    robots = [17,59,32,11,72,18]
    distance = [5,7,6,5,2,10]
    walls = [17,25,33,29,54,53,18,35,39,37,20,14,34,13,16,58,22,51,56,27,10,15,12,23,45,43,21,2,42,7,32,40,8,9,1,5,55,30,38,4,3,31,36,41,57,28,11,49,26,19,50,52,6,47,46,44,24,48]
    expected = 37
    assert Solution().maxWalls(robots, distance, walls) == expected