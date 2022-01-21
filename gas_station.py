"""
LeetCode :: January 2022 Challenge :: 134. Gas Station
jramaswami
"""


from typing import *
from itertools import repeat, chain


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Create cycle of two of each list.
        gas0 = chain.from_iterable(repeat(gas, 2))
        cost0 = chain.from_iterable(repeat(cost, 2))
        fuel_tank = 0
        start = 0
        for i, (g, c) in enumerate(zip(gas0, cost0)):
            if i == start + len(gas):
                return start
            fuel_tank += g
            if fuel_tank < c:
                fuel_tank = 0
                start = i + 1
            else:
                fuel_tank -= c
        return -1


def test_1():
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    expected = 3
    assert Solution().canCompleteCircuit(gas, cost) == expected


def test_2():
    gas = [2,3,4]
    cost = [3,4,3]
    expected = -1
    assert Solution().canCompleteCircuit(gas, cost) == expected
