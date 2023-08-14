"""
LeetCode
215. Kth Largest Element in an Array
August 2023 Challenge
jramaswami
"""


import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


def test_1():
    nums = [3,2,1,5,6,4]
    k = 2
    expected = 5
    assert Solution().findKthLargest(nums, k) == expected


def test_2():
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    expected = 4
    assert Solution().findKthLargest(nums, k) == expected