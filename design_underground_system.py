"""
LeetCode :: April 2022 Challenge :: Design Underground System
jramaswami
"""


import collections


class UndergroundSystem:

    def __init__(self):
        self.travel_time = collections.defaultdict(int)
        self.travel_freq = collections.defaultdict(int)
        self.curr_travelers = dict()

    def checkIn(self, cust_id: int, station_name: str, checkin_t: int) -> None:
        self.curr_travelers[cust_id] = (station_name, checkin_t)

    def checkOut(self, cust_id: int, station_name: str, checkout_t: int) -> None:
        prev_station, checkin_t = self.curr_travelers[cust_id]
        key = (prev_station, station_name)
        self.travel_freq[key] += 1
        self.travel_time[key] += checkout_t - checkin_t
        self.curr_travelers[cust_id] = None

    def getAverageTime(self, start_station: str, end_station: str) -> float:
        key = (start_station, end_station)
        return self.travel_time[key] / self.travel_freq[key]


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
