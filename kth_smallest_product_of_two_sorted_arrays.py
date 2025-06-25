"""
LeetCode
2040. Kth Smallest Product of Two Sorted Arrays
June 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Brute force
        A = [a * b for a in nums1 for b in nums2]
        A.sort()
        return A[k-1]


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