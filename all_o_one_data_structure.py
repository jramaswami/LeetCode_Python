"""
LeetCode :: 432. All O`one Data Structure
jramaswami
"""


import collections
import heapq


class MaxPQ:

    def __init__(self):
        self.heap = []

    def push(self, x, t):
        heapq.heappush(self.heap, (-x, t))

    def pop(self):
        item = heapq.heappop(self.heap)
        return (-item[0], item[1])

    def top(self):
        return (-self.heap[0][0], self.heap[0][1])

    def __len__(self):
        return len(self.heap)


class MinPQ:

    def __init__(self):
        self.heap = []

    def push(self, x, t):
        heapq.heappush(self.heap, (x, t))

    def pop(self):
        return heapq.heappop(self.heap)

    def top(self):
        return self.heap[0]

    def __len__(self):
        return len(self.heap)


class AllOne:

    def __init__(self):
        self.freqs = collections.Counter()
        self.minpq = MinPQ()
        self.maxpq = MaxPQ()

    def inc(self, key: str) -> None:
        self.freqs[key] += 1
        self.maxpq.push(self.freqs[key], key)
        self.minpq.push(self.freqs[key], key)

    def dec(self, key: str) -> None:
        self.freqs[key] -= 1
        self.maxpq.push(self.freqs[key], key)
        self.minpq.push(self.freqs[key], key)

    def getMaxKey(self) -> str:
        while self.maxpq.top()[0] != self.freqs[self.maxpq.top()[1]]:
            self.maxpq.pop()
        return "" if not self.maxpq else self.maxpq.top()[1]

    def getMinKey(self) -> str:
        while self.minpq.top()[0] != self.freqs[self.minpq.top()[1]]:
            self.minpq.pop()
        return "" if not self.minpq else self.minpq.top()[1]


#
# Testing
#


null = None   # To make pasting testcases easier.


def test_1():
    methods = ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
    arguments = [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
    expected = [null, null, null, "hello", "hello", null, "hello", "leet"]
    aoods = AllOne()
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        r = getattr(aoods, m)(*a)
        print(f"aaods.{m}({a}) = {r} ? {e}")
        assert r == e


def test_2():
    "RTE"
    methods = ["AllOne","getMaxKey","getMinKey"]
    arguments = [[],[],[]]
    expected = [None, None, None]
    aoods = AllOne()
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        r = getattr(aoods, m)(*a)
        print(f"aaods.{m}({a}) = {r} ? {e}")
        assert r == e