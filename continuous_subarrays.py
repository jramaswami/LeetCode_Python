"""
LeetCode
2762. Continuous Subarrays
December 2024 Challenge
jramaswami
"""


import collections
import dataclasses
import heapq


@dataclasses.dataclass(frozen=True)
class QItem:
    index: int
    value: int

    def __lt__(self, other):
        if self.value == other.value:
            return self.index < other.index
        return self.value < other.value


class MaxPQ:
    def __init__(self):
        self.heap = []
    
    def push(self, priority, item):
        heapq.heappush(self.heap, (-priority, item))
    
    def pop(self):
        _, item = heapq.heappop(self.heap)
        return item

    def top(self):
        _, item = self.heap[0]
        return item


class MinPQ:
    def __init__(self):
        self.heap = []
    
    def push(self, priority, item):
        heapq.heappush(self.heap, (priority, item))
    
    def pop(self):
        _, item = heapq.heappop(self.heap)
        return item

    def top(self):
        _, item = self.heap[0]
        return item


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        max_pq = MaxPQ()
        min_pq = MinPQ()
        window = collections.deque()
        soln = 0
        for i, n in enumerate(nums):
            item = QItem(i, n)
            max_pq.push(n, item)
            min_pq.push(n, item)
            window.append(item)
            while max_pq.top().value - min_pq.top().value > 2:
                xitem = window.popleft()
                while max_pq.top().index <= xitem.index:
                    max_pq.pop()
                while min_pq.top().index <= xitem.index:
                    min_pq.pop()
            soln += len(window)
        return soln
