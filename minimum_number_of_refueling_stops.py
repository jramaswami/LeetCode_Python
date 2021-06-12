"""
LeetCode :: June 2021 Challenge :: Minimum Number of Refueling Stop
jramaswami
"""


import heapq
from typing import *


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # Add "dummy" station for target.
        stations.append((target, 0))
        stops = 0
        auto_fuel = startFuel
        prev_fuels = []
        prev_location = 0
        for curr_location, station_fuel in stations:
            # Go to next station.
            distance = curr_location - prev_location
            auto_fuel = auto_fuel - distance
            # If auto ran out of fuel, go back in time to fuel up using
            # the largest fuel from previous stations.
            while auto_fuel < 0 and prev_fuels:
                refuel = -heapq.heappop(prev_fuels)
                auto_fuel = auto_fuel + refuel
                stops = stops + 1
            # If auto still has negative fuel, auto could not reach station.
            if auto_fuel < 0:
                return -1
            # "Remember" the fuel at current station.
            heapq.heappush(prev_fuels, -station_fuel)
            prev_location = curr_location
        return stops


def test_1():
    target = 1
    startFuel = 1
    stations = []
    expected = 0
    assert Solution().minRefuelStops(target, startFuel, stations) == expected


def test_2():
    target = 100
    startFuel = 1
    stations = [[10,100]]
    expected = -1 
    assert Solution().minRefuelStops(target, startFuel, stations) == expected


def test_3():
    target = 100
    startFuel = 10
    stations = [[10,60],[20,30],[30,30],[60,40]]
    expected = 2
    assert Solution().minRefuelStops(target, startFuel, stations) == expected


def test_4():
    """TLE"""
    target = 1000
    startFuel = 10
    stations = [[1,209],[2,30],[24,106],[25,3],[30,164],[33,4],[38,40],[56,202],[58,219],[69,90],[77,45],[78,90],[89,171],[94,26],[96,165],[109,122],[110,14],[121,142],[141,154],[150,196],[155,67],[159,246],[175,58],[203,71],[211,173],[226,64],[249,89],[272,74],[275,99],[276,205],[278,160],[279,203],[281,15],[282,72],[283,124],[295,90],[296,8],[307,120],[313,73],[327,15],[330,135],[331,87],[353,217],[364,120],[367,99],[371,152],[385,175],[392,241],[393,112],[399,125],[400,88],[409,187],[444,129],[448,158],[466,247],[468,153],[470,227],[474,129],[476,80],[477,198],[505,20],[529,125],[552,91],[553,59],[578,180],[587,142],[599,134],[617,224],[629,55],[649,79],[664,63],[669,236],[679,101],[694,108],[707,161],[717,32],[719,228],[721,95],[738,120],[747,59],[761,164],[769,153],[795,154],[802,236],[836,229],[849,247],[866,34],[874,45],[876,4],[880,31],[895,125],[908,188],[909,182],[911,62],[915,222],[928,34],[931,115],[934,165],[971,92],[993,221]]
    expected = 5
    assert Solution().minRefuelStops(target, startFuel, stations) == expected
