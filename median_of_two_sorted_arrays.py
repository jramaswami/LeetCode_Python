"""
LeetCode
4. Median of Two Sorted Arrays
jramaswami
REF: https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/#
"""


import math
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge array until it has enough for median
        m = ((len(nums1) + len(nums2)) // 2) + 1
        t = []
        left = 0
        right = 0
        while len(t) < m:
            if left >= len(nums1):
                t.append(nums2[right])
                right += 1
            elif right >= len(nums2):
                t.append(nums1[left])
                left += 1
            elif nums1[left] <= nums2[right]:
                t.append(nums1[left])
                left += 1
            else:
                t.append(nums2[right])
                right += 1

        if (len(nums1) + len(nums2)) % 2:
            return 1.0 * t[-1]
        return (t[-2] + t[-1]) / 2.0



EPS = pow(10, -6)


def test_1():
    nums1 = [1,3]
    nums2 = [2]
    expected = 2.0
    result = Solution().findMedianSortedArrays(nums1, nums2)
    assert abs(result - expected) < EPS


def test_2():
    nums1 = [1,2]
    nums2 = [3,4]
    expected = 2.50000
    result = Solution().findMedianSortedArrays(nums1, nums2)
    assert abs(result - expected) < EPS