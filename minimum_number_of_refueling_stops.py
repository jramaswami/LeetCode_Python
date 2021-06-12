"""
LeetCode :: June 2021 Challenge :: Minimum Number of Refueling Stop
jramaswami
"""


import heapq
from typing import *
from collections import namedtuple


Waypoint = namedtuple('Waypoint', ['stops', 'fuel', 'station'])
Station = namedtuple('Station', ['miles', 'fuel'])


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        Q = [Waypoint(0, startFuel, 0)]
        stations0 = [Station(0, 0)] + [Station._make(t) for t in stations]
        stations0.append(Station(target, 0))
        while Q:
            print(Q)
            curr_waypoint = heapq.heappop(Q)
            if curr_waypoint.station == len(stations0) - 1:
                return curr_waypoint.stops
            # Distance to next station
            distance = (stations0[curr_waypoint.station + 1].miles - 
                        stations0[curr_waypoint.station].miles
            )
            # Go to next station without refueling/stopping, if you can 
            # reach it.
            remaining_fuel = curr_waypoint.fuel - distance
            if remaining_fuel >= 0:
                nonstop_waypoint = Waypoint(curr_waypoint.stops,
                                            remaining_fuel,
                                            curr_waypoint.station + 1
                )
                heapq.heappush(Q, nonstop_waypoint)
            # Go to next station after stopping to refuel, if you can 
            # reach it.
            remaining_fuel = (curr_waypoint.fuel + 
                              stations0[curr_waypoint.station].fuel - 
                              distance
            )
            if remaining_fuel >= 0:
                refueled_waypoint = Waypoint(curr_waypoint.stops + 1,
                                            remaining_fuel,
                                            curr_waypoint.station + 1
                )
                heapq.heappush(Q, refueled_waypoint)

        return -1



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
