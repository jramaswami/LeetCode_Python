"""
LeetCode
1855. Maximum Distance Between a Pair of Values
April 2026 Challenge
jramaswami
"""


from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        soln = 0
        while i < len(nums1) and j < len(nums2):
            while i < len(nums1) and i <= j and nums1[i] > nums2[j]:
                i += 1
            if i < len(nums1) and i <= j and nums1[i] <= nums2[j]:
                soln = max(soln, j - i)
            j += 1
        return soln