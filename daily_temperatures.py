"""
LeetCode ::
739. Daily Temperatures
December 2022 Challenge
jramaswami
"""


import collections


Item = collections.namedtuple('Item', ['index', 'temp'])


class Solution:
    def dailyTemperatures(self, temperatures):
        soln = [0 for _ in temperatures]
        # Monoqueue invariant: temperatures from left to right are descending.
        monoqueue = []
        for i, t in enumerate(temperatures):
            curr_item = Item(i, t)
            while monoqueue and monoqueue[-1].temp < curr_item.temp:
                prev_item = monoqueue.pop()
                soln[prev_item.index] = curr_item.index - prev_item.index
            monoqueue.append(curr_item)
        return soln


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
