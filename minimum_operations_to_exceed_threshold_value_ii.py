"""
LeetCode
3066. Minimum Operations to Exceed Threshold Value II
February 2025 Challenge
jramaswami
"""


import heapq


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        soln = 0
        while nums[0] < k:
            soln += 1
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            t = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, t)
        return soln
