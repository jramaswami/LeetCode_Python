"""
LeetCode
70. Climbing Stairs
December 2022 Challenge
jramaswami
"""


import functools


class Solution:

    def climbStairs(self, steps):
        @functools.cache
        def solve(step):
            if step < 0:
                return 0
            if step == 0:
                return 1
            return solve(step-2) + solve(step-1)

        return solve(steps)


def test_1():
    assert Solution().climbStairs(2) == 2


def test_2():
    assert Solution().climbStairs(3) == 3


def test_3():
    assert Solution().climbStairs(45) == 1836311903
