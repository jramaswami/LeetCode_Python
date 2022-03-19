"""
LeetCode :: March 2022 Challenge :: Maximum Frequency Stack
jramaswami
"""


import collections
import heapq


class FreqStack:

    def __init__(self):
        # Stack is heap of (-freq, time, val)
        self.stack = []
        self.clock = 0
        self.freqs = collections.defaultdict(int)

    def push(self, x) -> None:
        self.clock += 1
        self.freqs[x] += 1
        heapq.heappush(self.stack, (-self.freqs[x], -self.clock, x))

    def pop(self) -> int:
        _, _, x = heapq.heappop(self.stack)
        self.freqs[x] -= 1
        return x


# Testing
null = None

def test_1():
    fs = FreqStack()
    fs.push(5)
    fs.push(7)
    fs.push(5)
    fs.push(7)
    fs.push(4)
    fs.push(5)
    assert fs.pop() == 5
    assert fs.pop() == 7
    assert fs.pop() == 5
    assert fs.pop() == 4

def test_2():
    calls = ["FreqStack","push","push","push","push","push","push","pop","push","pop","push","pop","push","pop","push","pop","pop","pop","pop","pop","pop"]
    args = [[],[4],[0],[9],[3],[4],[2],[],[6],[],[1],[],[1],[],[4],[],[],[],[],[],[]]
    expected = [null,null,null,null,null,null,null,4,null,6,null,1,null,1,null,4,2,3,9,0,4]
    fs = FreqStack()
    for call, arg, exp in zip(calls[1:], args[1:], expected[1:]):
        assert getattr(fs, call)(*arg) == exp
