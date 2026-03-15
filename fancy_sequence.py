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
        self.MOD = pow(10, 9) + 7

    def inverse(self, a):
        return pow(a, self.MOD-2, self.MOD)

    def append(self, val: int) -> None:
        self.values.append(Value(len(self.additions), val))

    def addAll(self, inc: int) -> None:
        self.additions.append((self.additions[-1] + inc) % self.MOD)
        self.multiplications.append(self.multiplications[-1])

    def multAll(self, m: int) -> None:
        self.additions.append((self.additions[-1] * m) % self.MOD)
        self.multiplications.append((self.multiplications[-1] * m) % self.MOD)

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.values):
            return -1

        value = self.values[idx]
        if value.clock == 1:
            x = (value.val * self.multiplications[-1]) + self.additions[-1]
        else:
            m = self.multiplications[-1] * self.inverse(self.multiplications[value.clock-1])
            p = (self.additions[value.clock-1] * m) % self.MOD
            a = (self.additions[-1] - p + self.MOD) % self.MOD
            x = (value.val * m) + a
        return x % self.MOD