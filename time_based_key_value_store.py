"""
LeetCode :: October 2022 Challenge :: 981. Time Based Key-Value Store
jramaswami
"""


import collections


DataItem = collections.namedtuple('DataItem', ['timestamp', 'value'])


class TimeMap:

    def __init__(self):
        self.data = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append(DataItem(timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # Binary search
        result = None
        if key in self.data:
            lo = 0
            hi = len(self.data[key]) - 1
            while lo <= hi:
                mid = lo + ((hi - lo) // 2)
                if self.data[key][mid].timestamp <= timestamp:
                    result = self.data[key][mid].value
                    lo = mid + 1
                else:
                    hi = mid - 1
        return result


#
# Testing
#


null = None


def test_1():
    methods = ["TimeMap", "set", "get", "get", "set", "get", "get"]
    arguments = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
    expected = [null, null, "bar", "bar", null, "bar2", "bar2"]
    tm = TimeMap()
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        assert getattr(tm, m)(*a) == e


def test_2():
    "WA"
    methods = ["TimeMap","set","set","get","get","get","get","get"]
    arguments = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
    expected = [null,null,null,"","high","high","low","low"]
    tm = TimeMap()
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        assert getattr(tm, m)(*a) == e