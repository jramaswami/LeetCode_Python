"""
LeetCode
239. Sliding Window Maximum
August 2023 Challenge
jramaswami
"""


import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = []
        soln = []
        for i, n in enumerate(nums):
            heapq.heappush(pq, (-n, i))
            while pq[0][1] <= i - k:
                heapq.heappop(pq)
            if len(pq) >= k:
                soln.append(-pq[0][0])
        return soln


def test_1():
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    expected = [3,3,5,5,6,7]
    assert Solution().maxSlidingWindow(nums, k) == expected


def test_2():
    nums = [1]
    k = 1
    expected = [1]
    assert Solution().maxSlidingWindow(nums, k) == expected