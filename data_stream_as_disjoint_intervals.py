"""
LeetCode
352. Data Stream as Disjoint Intervals
January 2023 Challenge
jramaswami
"""


from typing import *
import collections


class UnionFind:

    def __init__(self):
        self.parent = collections.defaultdict(int)
        self.range_end = dict()

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.range_end[x] = x
            if x-1 in self.parent:
                self.join(x-1, x)
            if x+1 in self.parent:
                self.join(x, x+1)

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def join(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            if a > b:
                a, b = b, a
            self.parent[b] = a
            self.range_end[a] = max(self.range_end[a], self.range_end[b])
            del self.range_end[b]


class SummaryRanges:

    def __init__(self):
        self.uf = UnionFind()

    def addNum(self, value: int) -> None:
        self.uf.add(value)

    def getIntervals(self) -> List[List[int]]:
        return [[x, self.uf.range_end[x]] for x in sorted(self.uf.range_end)]


null = None


def test_1():
    methods = [
        "SummaryRanges", "addNum", "getIntervals", "addNum",
        "getIntervals", "addNum", "getIntervals", "addNum",
        "getIntervals", "addNum", "getIntervals"
    ]
    arguments = [[], [1], [], [3], [], [7], [], [2], [], [6], []]
    expected = [
        null, null, [[1, 1]], null, [[1, 1], [3, 3]], null,
        [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]],
        null, [[1, 3], [6, 7]]
    ]
    solver = SummaryRanges()
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        assert getattr(solver, m)(*a) == e


def test_2():
    "WA"
    methods = [
        "SummaryRanges","addNum","getIntervals","addNum","getIntervals",
        "addNum","getIntervals","addNum","getIntervals","addNum","getIntervals",
        "addNum","getIntervals","addNum","getIntervals","addNum","getIntervals",
        "addNum","getIntervals","addNum","getIntervals"
    ]
    arguments = [
        [],[6],[],[6],[],[0],[],[4],[],[8],[],[7],[],[6],[],[4],[],[7],[],[5],[]
    ]
    expected = [
        null,null,[[6,6]],null,[[6,6]],null,[[0,0],[6,6]],null,
        [[0,0],[4,4],[6,6]],null,[[0,0],[4,4],[6,6],[8,8]],null,
        [[0,0],[4,4],[6,8]],null,[[0,0],[4,4],[6,8]],null,
        [[0,0],[4,4],[6,8]],null,[[0,0],[4,4],[6,8]],null,[[0,0],[4,8]]
    ]
    solver = SummaryRanges()
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        r = getattr(solver, m)(*a)
        print(m, a, e, r)
        assert r == e