"""
LeetCode :: March 2022 Challenge :: Broken Calculator
jramaswami
"""


class Solution:
    def brokenCalc(self, X, Y):
        # Boundary case.
        if X == Y:
            return 0

        soln = 0
        while Y > X:
            soln += 1
            if Y % 2:
                Y += 1
            else:
                Y //= 2

        return soln + X - Y


def test_1():
    assert Solution().brokenCalc(2, 3) == 2


def test_2():
    assert Solution().brokenCalc(5, 8) == 2


def test_3():
    assert Solution().brokenCalc(3, 10) == 3


def test_4():
    assert Solution().brokenCalc(1024, 1) == 1023
