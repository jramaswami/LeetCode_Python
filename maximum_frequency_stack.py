"""
LeetCode :: Maximum Frequency Stack
jramaswami
"""
from collections import defaultdict
import heapq


class FreqStack:

    def __init__(self):
        self.queue = []
        self.freqs = defaultdict(int)
        self.timer = -1
        
    def push(self, x: int) -> None:
        self.freqs[x] += 1
        heapq.heappush(self.queue, (-self.freqs[x], self.timer, x))
        self.timer -=1
        
    def pop(self) -> int:
        _, _, x = heapq.heappop(self.queue)
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
        print(fs.freqs)
        print(fs.queue)
        print(call, arg, exp)
        assert getattr(fs, call)(*arg) == exp
