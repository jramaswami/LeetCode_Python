"""
LeetCode
945. Minimum Increment to Make Array Unique
jramaswami
"""


import heapq
from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        soln = 0
        heapq.heapify(nums)
        stack = [heapq.heappop(nums)]
        while nums:
            x = heapq.heappop(nums)
            if x == stack[-1]:
                heapq.heappush(nums, x + 1)
                soln += 1
            else:
                stack.append(x)
        return soln 
