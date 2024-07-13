"""
LeetCode
2751. Robot Collisions
July 2024 Challenge
jramaswami
"""


import collections
import operator


Robot = collections.namedtuple('Robot', ['position', 'health', 'direction', 'index'])


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        
        def survive(robot):
            return Robot(robot.position, robot.health - 1, robot.direction, robot.index)

        robots = [Robot(p, h, d, i) for i, (p, h, d) in enumerate(zip(positions, healths, directions))]
        robots.sort()

        stack = []
        for robot in robots:
            # If robot is moving left, remove results of collision
            if robot.direction == 'L':
                while stack and robot and stack[-1].direction == 'R':
                    # Collision
                    if stack[-1].health < robot.health:
                        stack.pop()
                        robot = survive(robot)
                    elif stack[-1].health > robot.health:
                        stack[-1] = survive(stack[-1])
                        robot = None
                    else:
                        stack.pop()
                        robot = None
            
            # If robot survives, place it on the stack
            if robot:
                stack.append(robot)
        
        stack.sort(key=operator.attrgetter('index'))
        return [r.health for r in stack]
