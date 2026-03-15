"""
LeetCode
1622. Fancy Sequence
March 2026 Challenge
jramaswami
"""


import collections


Operation = collections.namedtuple('Operation', ('clock', 'fn'))
Value = collections.namedtuple('Value', ('clock', 'val'))

class Fancy:

    def __init__(self):
        self.additions = [0]
        self.multiplications = [1]
        self.values = []

    def append(self, val: int) -> None:
        self.values.append(Value(len(self.additions), val))

    def addAll(self, inc: int) -> None:
        self.additions.append(inc)
        self.multiplications.append(self.multiplications[-1])

    def multAll(self, m: int) -> None:
        self.additions.append(self.additions[-1] * m)
        self.multiplications.append(self.multiplications[-1] * m)

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.values):
            return -1
        m = self.multiplications[-1] // self.multiplications[idx-1]
        a = self.additions[idx-1] * m
        x = (self.additions[-1] - a) // m
        return x
