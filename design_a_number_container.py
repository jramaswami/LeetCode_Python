"""
LeetCode
2349. Design a Number Container System
February 2025 Challenge
jramaswami
"""


import collections
import heapq


class NumberContainers:

    def __init__(self):
        self.container = collections.defaultdict(int)
        self.indexes = collections.defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.container[index] = number
        heapq.heappush(self.indexes[number], index)

    def find(self, number: int) -> int:
        # Get rid of the indexes at the front of the heapq that are no longer valid
        while self.indexes[number]:
            index = self.indexes[number][0]
            if self.container[index] == number:
                break
            heapq.heappop(self.indexes[number])
        if self.indexes[number]:
            return self.indexes[number][0]
        return -1
