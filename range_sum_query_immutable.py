"""
LeetCode :: August 2021 Challenge :: Range Sum Query - Immutable
jramaswami
"""

import itertools


class NumArray:

    def __init__(self, nums):
        self.prefix = list(itertools.accumulate(nums))
        print(self.prefix)


    def _get(self, i):
        if i < 0:
            return 0
        return self.prefix[i]

    def sumRange(self, left, right):
        return self._get(right) - self._get(left - 1)


def test_1():
    methods = ["NumArray", "sumRange", "sumRange", "sumRange"]
    arguments = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
    expected = [None, 1, -1, -3]
    A = NumArray(*arguments[0])
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        r = getattr(A, m)(*a)
        assert r == e
