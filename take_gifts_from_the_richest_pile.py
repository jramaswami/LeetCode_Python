"""
LeetCode
2558. Take Gifts From the Richest Pile
December 2024 Challenge
jramaswami
"""


import heapq
import math
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        for g in gifts:
            heapq.heappush(heap, -g)
        for _ in range(k):
            g = -heapq.heappop(heap)
            h = int(math.sqrt(g))
            heapq.heappush(heap, -h)
        return sum(-x for x in heap)
