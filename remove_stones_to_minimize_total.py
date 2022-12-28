"""
LeetCode
1962. Remove Stones to Minimize the Total
jramaswami
"""


import heapq
from typing import *


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        print(piles)
        heap = [-p for p in piles]
        heapq.heapify(heap)
        for _ in range(k):
            p = -heapq.heappop(heap)
            q = p - (p // 2)
            heapq.heappush(heap, -q)
        return -sum(heap)


def test_1():
    piles = [5,4,9]
    k = 2
    expected = 12
    assert Solution().minStoneSum(piles, k) == expected


def test_2():
    piles = [4,3,6,7]
    k = 3
    expected = 12
    assert Solution().minStoneSum(piles, k) == expected
