"""
LeetCode
373. Find K Pairs with Smallest Sums
June 2023 Challenge
jramaswami
"""


import collections
import heapq
from typing import List


QItem = collections.namedtuple('QItem', ['sum', 'i', 'j'])


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for i, n in enumerate(nums1):
            heapq.heappush(heap, QItem(n + nums2[0], i, 0))
        soln = []
        for _ in range(k):
            if not heap:
                break
            item = heapq.heappop(heap)
            soln.append([nums1[item.i], nums2[item.j]])
            if item.j + 1 < len(nums2):
                heapq.heappush(heap, QItem(nums1[item.i] + nums2[item.j+1], item.i, item.j+1))
        return soln


def test_1():
    nums1 = [1,7,11]
    nums2 = [2,4,6]
    k = 3
    expected = [[1,2],[1,4],[1,6]]
    assert Solution().kSmallestPairs(nums1, nums2, k) == expected


def test_2():
    nums1 = [1,1,2]
    nums2 = [1,2,3]
    k = 2
    expected = [[1,1],[1,1]]
    assert Solution().kSmallestPairs(nums1, nums2, k) == expected


def test_3():
    nums1 = [1,2]
    nums2 = [3]
    k = 3
    expected = [[1,3],[2,3]]
    assert Solution().kSmallestPairs(nums1, nums2, k) == expected
