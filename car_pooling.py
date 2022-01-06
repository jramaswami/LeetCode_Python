"""
LeetCode :: January 2022 Challenge :: 1094. Car Pooling
jramaswami
"""


import collections
import enum
from typing import *



class EType(enum.IntEnum):
    EMBARK = 1
    DISEMBARK = -1


Event = collections.namedtuple('Event', ['stop', 'type', 'passengers'])


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for num_passengers, embark_stop, disembark_stop in trips:
            events.append(Event(embark_stop, EType.EMBARK, num_passengers))
            events.append(Event(disembark_stop, EType.DISEMBARK, num_passengers))
        events.sort()
        curr = 0
        for stop, etype, passengers in events:
            curr += (etype * passengers)
            if curr > capacity:
                return False
        return True


def test_1():
    trips = [[2,1,5],[3,3,7]]
    capacity = 4
    assert Solution().carPooling(trips, capacity) == False


def test_2():
    trips = [[2,1,5],[3,3,7]]
    capacity = 5
    assert Solution().carPooling(trips, capacity) == True
