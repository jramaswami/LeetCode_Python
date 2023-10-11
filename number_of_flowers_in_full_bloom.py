"""
LeetCode
2251. Number of Flowers in Full Bloom
October 2023 Challenge
jramaswami
"""


import collections
import operator
from typing import List


Event = collections.namedtuple('Event', ['time', 'delta'])
Person = collections.namedtuple('Person', ['arrives', 'index'])


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # Create list of events
        events = []
        for blooms, dies in flowers:
            events.append(Event(blooms, 1))
            events.append(Event(dies+1, -1))

        # Sort events by time (in reverse)
        events.sort(key=operator.attrgetter('time'), reverse=True)
        print(events)

        # Sort the people arriving
        people0 = [Person(t, i) for i, t in enumerate(people)]
        people0.sort(key=operator.attrgetter('arrives'))
        soln = [0 for _ in people]

        flowers_in_bloom = 0
        for person in people0:
            while events and events[-1].time <= person.arrives:
                flowers_in_bloom += events[-1].delta
                events.pop()
            soln[person.index] = flowers_in_bloom

        return soln


def test_1():
    flowers = [[1,6],[3,7],[9,12],[4,13]]
    people = [2,3,7,11]
    expected = [1,2,2,2]
    assert Solution().fullBloomFlowers(flowers, people) == expected


def test_2():
    flowers = [[1,10],[3,3]]
    people = [3,3,2]
    expected = [2,2,1]
    assert Solution().fullBloomFlowers(flowers, people) == expected