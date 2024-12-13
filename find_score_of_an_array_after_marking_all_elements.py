"""
LeetCode
2593. Find Score of an Array After Marking All Elements
December 2024 Challenge
jramaswami
"""


import heapq
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap = []
        for i, n in enumerate(nums):
            heapq.heappush(heap, (n, i))
        marked = [False for _ in nums]
        score = 0
        while heap:
            n, i = heapq.heappop(heap)
            if not marked[i]:
                score += n
                marked[i] = True
                if i - 1 >= 0:
                    marked[i-1] = True
                if i + 1 < len(nums):
                    marked[i+1] = True
        return score
