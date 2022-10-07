"""
LeetCode :: October 2022 Challenge :: 732. My Calendar III
jramaswami
"""


import sortedcontainers


class Event:

    START = 1
    STOP = -1

    def __init__(self, timer, etype):
        self.etype = etype
        self.timer = timer

    def __lt__(self, other):
        if self.timer == other.timer:
            return self.etype < other.etype
        return self.timer < other.timer


class MyCalendarThree:

    def __init__(self):
        self.intervals = sortedcontainers.SortedList()

    def book(self, start: int, end: int) -> int:
        self.intervals.add(Event(start, Event.START))
        self.intervals.add(Event(end, Event.STOP))

        curr = 0
        result = 0
        for event in self.intervals:
            curr += event.etype
            result = max(result, curr)
        return result


#
# TESTING
#


null = None


def test_1():
    methods = ["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
    arguments = [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
    expected = [null, 1, 1, 2, 3, 3, 3]
    mc = MyCalendarThree()
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        assert getattr(mc, m)(*a) == e