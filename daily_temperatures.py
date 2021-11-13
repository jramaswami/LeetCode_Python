"""
LeetCode :: November 2021 Challenge :: 739. Daily Temperatures
jramaswami

Thank you Larry!
"""


import collections


SItem = collections.namedtuple('SItem', ['temperature', 'index'])


class Solution:
    def dailyTemperatures(self, temperatures):
        answers = [len(temperatures) for _ in temperatures]
        stack = []
        for i in range(len(temperatures) - 1, -1, -1):
            # Remove any values smaller than temperature[i] because they
            # will not be the nearest higher temperature to anything to
            # the left of temperatures[i] because temperatures[i] will be.
            while stack and stack[-1].temperature <= temperatures[i]:
                stack.pop()

            if stack:
                # The only remaining items on the stack are greater than
                # temperatures[i].  The top of the stack will be the first
                # temperature higher than temperatures[i].
                answers[i] = stack[-1].index - i
            else:
                # There is nothing on the stack, therefore, there is no answer
                # for temperatures[i].
                answers[i] = 0

            # Add temperatures[i] to the stack.
            stack.append(SItem(temperatures[i], i))

        return answers


def test_1():
    temperatures = [73,74,75,71,69,72,76,73]
    expected = [1,1,4,2,1,1,0,0]
    assert Solution().dailyTemperatures(temperatures) == expected


def test_2():
    temperatures = [30,40,50,60]
    expected = [1,1,1,0]
    assert Solution().dailyTemperatures(temperatures) == expected


def test_3():
    temperatures = [30,60,90]
    expected = [1,1,0]
    assert Solution().dailyTemperatures(temperatures) == expected


def test_4():
    """TLE"""
    N = pow(10, 5)
    temperatures = [30] * (N - 1)
    temperatures.append(31)
    expected = list(reversed(range(1, N)))
    expected.append(0)
    assert Solution().dailyTemperatures(temperatures) == expected