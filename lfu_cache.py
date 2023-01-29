"""
LeetCode
460. LFU Cache
January 2023 Challenge
jramaswami
"""


from typing import *
import heapq
import itertools
import collections


Item = collections.namedtuple('Item', ['freq_used', 'last_used', 'key'])


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.heap = []
        self.last_used = dict()
        self.freq_used = dict()
        self.values = dict()
        self.timer = itertools.count()

    def get(self, key: int) -> int:
        if key in self.values:
            self.last_used[key] = next(self.timer)
            self.freq_used[key] += 1
            heapq.heappush(self.heap, Item(self.freq_used[key], self.last_used[key], key))
            return self.values[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.values:
            self.last_used[key] = next(self.timer)
            self.freq_used[key] += 1
            self.values[key] = value
            heapq.heappush(self.heap, Item(self.freq_used[key], self.last_used[key], key))
        else:
            while self.heap and len(self.values) > self.capacity - 1:
                item_to_delete = heapq.heappop(self.heap)
                if item_to_delete.last_used == self.last_used[item_to_delete.key]:
                    del self.values[item_to_delete.key]
                    self.freq_used[item_to_delete.key] = 0
                    self.last_used[item_to_delete.key] = -1
            if len(self.heap) < self.capacity:
                self.last_used[key] = next(self.timer)
                self.freq_used[key] = 1
                self.values[key] = value
                heapq.heappush(self.heap, Item(self.freq_used[key], self.last_used[key], key))


null = None


def test_1():
    methods = ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
    arguments = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
    expected = [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
    lfucache = LFUCache(*arguments[0])
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        r = getattr(lfucache, m)(*a)
        assert r == e

def test_2():
    "RTE"
    methods = ["LFUCache","put","get"]
    arguments = [[0],[0,0],[0]]
    expected = [null, null, -1]
    lfucache = LFUCache(*arguments[0])
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        r = getattr(lfucache, m)(*a)
        assert r == e


def test_3():
    "WA"
    methods = ["LFUCache","put","put","get","get","get","put","put","get","get","get","get"]
    arguments = [[3],[2,2],[1,1],[2],[1],[2],[3,3],[4,4],[3],[2],[1],[4]]
    expected = [null,null,null,2,1,2,null,null,-1,2,1,4]
    lfucache = LFUCache(*arguments[0])
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        r = getattr(lfucache, m)(*a)
        assert r == e