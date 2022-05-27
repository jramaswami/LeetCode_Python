"""
LeetCode :: May 2022 Challenge :: 1342. Number of Steps to Reduce a Number to Zero
jramaswami
"""


class Solution:

    def numberOfSteps(self, n):
        steps = 0
        while n:
            steps += 1
            if n % 2:
                n -= 1
            else:
                n //= 2
        return steps


def test_1():
    num = 14
    expected = 6
    assert Solution().numberOfSteps(num) == expected


def test_2():
    num = 8
    expected = 4
    assert Solution().numberOfSteps(num) == expected


def test_3():
    num = 123
    expected = 12
    assert Solution().numberOfSteps(num) == expected
