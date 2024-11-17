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
        queue = collections.deque() # (prefix_sum, end_index)
        soln = math.inf
        curr_sum = 0
        for i, n in enumerate(nums):
            curr_sum += n
            if curr_sum >= k:
                soln = min(soln, i+1)
            # Find the minimum valid window ending at i
            while queue and curr_sum - queue[0][0] >= k:
                _, j = queue.popleft()
                soln = min(soln, i - j)
            # Maintain monotonic queue
            while queue and queue[-1][0] > curr_sum:
                queue.pop()
            queue.append((curr_sum, i))
            
        return -1 if soln == math.inf else soln
