"""
LeetCode
2211. Count Collisions on a Road
December 2025 Challenge
jramaswami
"""


class Solution:
    def countCollisions(self, directions: str) -> int:
        collisions = 0
        stack = ['X']
        for car in directions:
            if car == 'S' and stack[-1] == 'R':
                collisions += 1
                stack[-1] = 'S'
                stack.append('S')
            elif car == 'L' and stack[-1] == 'R':
                collisions += 2
                stack[-1] = 'S'
                stack.append('S')
            elif car == 'L' and stack[-1] == 'S':
                collisions += 1
                stack[-1] = 'S'
                stack.append('S')
            else:
                stack.append(car)

        # Count any cars stuck behind crashes
        while stack[-1] == 'R':
            stack.pop()
        collisions += stack.count('R')
        return collisions


def test_1():
    directions = "RLRSLL"
    expected = 5
    assert Solution().countCollisions(directions) == expected


def test_2():
    directions = "LLRR"
    expected = 0
    assert Solution().countCollisions(directions) == expected


def test_3():
    "WA"
    directions = "SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR"
    expected = 20
    assert Solution().countCollisions(directions) == expected