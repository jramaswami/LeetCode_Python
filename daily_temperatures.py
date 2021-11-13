"""
LeetCode :: November 2021 Challenge :: 739. Daily Temperatures
jramaswami

There are only 100 - 30 or 70 possible temperators.  Moving from right
to left, we can keep track of the rightmost index of any existing
temperatures.  For each index we can search from temperatures[i]+1 to 100
for the next temperature greater.  This will be O(70 * N) or O(N).
"""


import math


class Solution:
    def dailyTemperatures(self, temperatures):
        following_temperatures = dict()
        answers = [math.inf for _ in temperatures]
        for i in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[i]
            for t in range(temp+1, 101):
                answers[i] = min(
                    answers[i],
                    following_temperatures.get(t, math.inf) - i
                )
            following_temperatures[temp] = i
        return [0 if i == math.inf else i for i in answers]


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