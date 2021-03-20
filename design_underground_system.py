"""
LeetCode :: March 2021 Challenge :: Design Underground System
jramaswami
"""
from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.travelers = dict()
        self.travel_times = defaultdict(int)
        self.travel_freqs = defaultdict(int)
        
    def checkIn(self, custid: int, stationName: str, t: int) -> None:
        self.travelers[custid] = (stationName, t)
        
    def checkOut(self, custid: int, stationName: str, t: int) -> None:
        stationName0, checkInTime = self.travelers[custid]
        del self.travelers[custid]
        if stationName0 > stationName:
            stationName0, stationName = stationName, stationName0
        key = (stationName0, stationName)
        self.travel_times[key] += t - checkInTime
        self.travel_freqs[key] += 1
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if startStation > endStation:
            startStation, endStation = endStation, startStation
        key = (startStation, endStation)
        result = self.travel_times[key] / self.travel_freqs[key]
        return result


#
# Testing
#
null = None

def test_1():
    ugs = UndergroundSystem()
    ops = ["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
    args = [[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]
    expected = [null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]
    for o, a, e in zip(ops[1:], args[1:], expected[1:]):
        result = getattr(ugs, o)(*a)
        if result is not None:
            assert (abs(e - result) < 0.0001)
        else:
            assert result == e

def test_2():
    ugs = UndergroundSystem()
    ops = ["UndergroundSystem","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime"]
    args = [[],[10,"Leyton",3],[10,"Paradise",8],["Leyton","Paradise"],[5,"Leyton",10],[5,"Paradise",16],["Leyton","Paradise"],[2,"Leyton",21],[2,"Paradise",30],["Leyton","Paradise"]]
    expected = [null,null,null,5.00000,null,null,5.50000,null,null,6.66667]
    for o, a, e in zip(ops[1:], args[1:], expected[1:]):
        result = getattr(ugs, o)(*a)
        if result is not None:
            assert (abs(e - result) < 0.0001)
        else:
            assert result == e
