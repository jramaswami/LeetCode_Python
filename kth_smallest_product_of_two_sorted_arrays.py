"""
LeetCode
2040. Kth Smallest Product of Two Sorted Arrays
June 2025 Challenge
jramaswami

Thank You Larry!
"""


import bisect
import math
from typing import List


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # looking for a * b < x
        # if a > 0 then
        #   b < x / a
        # if a < 0 then binary (signs switched because a is negative)
        #   b > x / a
        # if a = 0 then
        #   all a * b = 0
        def count_smaller_products(target):
            smaller = 0
            for a in nums1:
                if a < 0:
                    smaller += len(nums2) - bisect.bisect_left(nums2, math.ceil(target / a))
                elif a == 0:
                    if target >= 0:
                        smaller += len(nums2)
                else:
                    smaller += bisect.bisect_right(nums2, target // a)
            return smaller

        def good(target):
            return count_smaller_products(target) >= k

        # Binary search the answer
        low = -pow(10, 10)
        high = pow(10, 10)
        while low < high:
            mid = low + ((high - low) // 2)
            if good(mid):
                high = mid
            else:
                low = mid + 1
        return low



def test_1():
    nums1 = [2,5]
    nums2 = [3,4]
    k = 2
    expected = 8
    assert Solution().kthSmallestProduct(nums1, nums2, k) == expected


def test_2():
    nums1 = [-4,-2,0,3]
    nums2 = [2,4]
    k = 6
    expected = 0
    assert Solution().kthSmallestProduct(nums1, nums2, k) == expected


def test_3():
    nums1 = [-2,-1,0,1,2]
    nums2 = [-3,-1,2,4,5]
    k = 3
    expected = -6
    assert Solution().kthSmallestProduct(nums1, nums2, k) == expected