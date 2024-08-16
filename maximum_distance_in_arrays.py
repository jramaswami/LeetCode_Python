"""
LeetCode
624. Maximum Distance in Arrays
August 2024 Challenge
jramaswami
"""


import heapq


class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def peek(self):
        return -self.heap[0]

    def push(self, x):
        heapq.heappush(self.heap, -x)


class MinHeap:
    def __init__(self):
        self.heap = []
    
    def peek(self):
        return self.heap[0]

    def push(self, x):
        heapq.heappush(self.heap, x)


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_heap = MinHeap()
        max_heap = MaxHeap()
        min_heap.push(arrays[0][0])
        max_heap.push(arrays[0][-1])
        soln = -pow(10, 10)
        for arr in arrays[1:]:
            soln = max(soln, abs(min_heap.peek() - arr[-1]))
            soln = max(soln, abs(max_heap.peek() - arr[0]))
            min_heap.push(arr[0])
            max_heap.push(arr[-1])
        return soln
