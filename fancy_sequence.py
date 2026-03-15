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
        self.operations = []
        self.clock = 0
        self.values = []
        self.MOD = pow(10, 9) + 7

    def append(self, val: int) -> None:
        self.values.append(Value(self.clock, val))
        self.clock += 1

    def addAll(self, inc: int) -> None:
        self.operations.append(Operation(self.clock, lambda x: x + inc))
        self.clock += 1

    def multAll(self, m: int) -> None:
        self.operations.append(Operation(self.clock, lambda x: x * m))
        self.clock += 1

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.values):
            return -1
        x = self.values[idx].val
        t = self.values[idx].clock
        for op in self.operations:
            if op.clock > t:
                x = op.fn(x)
                x %= self.MOD
        return x