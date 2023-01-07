"""
LeetCode
134. Gas Station
January 2022 Challenge
jramaswami
"""


from typing import *


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        def can_make_it(start_station):
            """
            Return True if the car can make it from start_station
            around the track.
            """
            curr_station = start_station
            curr_gas = 0
            for _ in gas:
                curr_gas += gas[curr_station]
                curr_gas -= cost[curr_station]
                if curr_gas < 0:
                    return False
                curr_station = (curr_station + 1) % len(gas)
            return True

        for start_station, _ in enumerate(gas):
            if can_make_it(start_station):
                return start_station
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