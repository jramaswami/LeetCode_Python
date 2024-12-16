"""
LeetCode
3264. Final Array State After K Multiplication Operations I
December 2024 Challenge
jramaswami
"""


import heapq


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        nums0 = [(x, i) for i, x in enumerate(nums)]
        heapq.heapify(nums0)
        for _ in range(k):
            x, i = heapq.heappop(nums0)
            x *= multiplier
            heapq.heappush(nums0, (x, i))
        nums1 = [0 for _ in nums]
        while nums0:
            x, i = heapq.heappop(nums0)
            nums1[i] = x
        return nums1
