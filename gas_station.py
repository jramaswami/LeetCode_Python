"""
LeetCode
134. Gas Station
January 2022 Challenge
jramaswami
"""


from typing import *


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        curr_start = 0
        curr_gas = 0
        for i in range(2*N):
            print(i, curr_gas)
            # Did the car make it to this station?
            if curr_gas < 0:
                # If it did not, then reset start to this station.
                # If we cannot make it to this station from the starting
                # station then we cannot make it from any of the other
                # previous stations either.
                curr_start = i
                curr_gas = 0
            # Did we reach the end?
            if i == curr_start + N:
                return curr_start
            # Fill up at this station and travel to the next.
            curr_gas += gas[i % N]
            curr_gas -= cost[i % N]
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