"""
LeetCode
1404. Number of Steps to Reduce a Number in Binary Representation to One
May 2024 Challenge
jramaswami
"""


class Solution:
    def numSteps(self, s: str) -> int:
        t = [int(x) for x in s]
        soln = 0
        while len(t) > 1:
            if t[-1] == 1:
                # Add one.
                t[-1] += 1
                soln += 1

            if t[-1] == 2:
                # Carry to next position
                t[-2] += 1
                t[-1] = 0

            if t[-1] == 0:
                # Divide by 2
                t.pop()
                soln += 1

        if t[0] == 2:
            # Divide by 2, if necessary
            soln += 1

        return soln


def test_1():
    s = "1101"
    expected = 6
    assert Solution().numSteps(s) == expected


def test_2():
    s = "10"
    expected = 1
    assert Solution().numSteps(s) == expected


def test_3():
    s = "1"
    expected = 0
    assert Solution().numSteps(s) == expected