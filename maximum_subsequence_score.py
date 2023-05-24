"""
LeetCode
2542. Maximum Subsequence Score
May 2023 Challenge
jramaswami
"""


import heapq
import math
import operator
from typing import *


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        heap = []
        curr_sum = 0
        soln = -math.inf
        values = list(zip(nums1, nums2))
        values.sort(key=operator.itemgetter(1), reverse=True)
        for num1, num2 in values:
            curr_sum += num1
            heapq.heappush(heap, -num1)
            while len(heap) > k:
                curr_sum += heapq.heappop(heap)
            if len(heap) == k:
                soln = max(soln, num2 * curr_sum)
        return soln


def test_1():
    nums1 = [1,3,3,2]
    nums2 = [2,1,3,4]
    k = 3
    expected = 12
    assert Solution().maxScore(nums1,nums2, k) == expected


def test_2():
    nums1 = [4,2,3,1,1]
    nums2 = [7,5,10,9,6]
    k = 1
    expected = 30
    assert Solution().maxScore(nums1,nums2, k) == expected


def test_3():
    nums1 = [2,1,14,12]
    nums2 = [11,7,13,6]
    k = 3
    expected = 168
    assert Solution().maxScore(nums1,nums2, k) == expected
