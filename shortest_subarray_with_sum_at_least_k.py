"""
LeetCode
862. Shortest Subarray with Sum at Least K
November 2024 Challenge
jramaswami

Thank You NeetCode.IO
"""


import collections
import heapq
import math


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        heap = []  # (prefix_sum, end_index)
        soln = math.inf
        curr_sum = 0
        for i, n in enumerate(nums):
            curr_sum += n
            if curr_sum >= k:
                soln = min(soln, i+1)
            # Find the minimum window ending at i
            while heap and curr_sum - heap[0][0] >= k:
                x, j = heapq.heappop(heap)
                soln = min(soln, i - j)
            heapq.heappush(heap, (curr_sum, i))
        return -1 if soln == math.inf else soln
