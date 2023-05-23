"""
LeetCode
May 2023 Challenge
Kth Largest Element in a Stream
jramaswami
"""


import heapq


class KthLargest:

    def __init__(self, k, nums):
        self.heap = list(nums)
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
