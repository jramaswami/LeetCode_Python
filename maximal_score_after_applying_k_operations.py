"""
LeetCode
2530. Maximal Score After Applying K Operations
October 2024 Challenge
jramaswami
"""


import heapq


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums0 = [-n for n in nums]
        heapq.heapify(nums0)
        soln = 0
        for _ in range(k):
            n = -heapq.heappop(nums0)
            soln += n
            n = ceil(n / 3)
            heapq.heappush(nums0, -n)
        return soln