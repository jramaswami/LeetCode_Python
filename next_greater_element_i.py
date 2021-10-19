"""
LeetCode :: October 2021 Challenge :: 496. Next Greater Element I
jramaswami
"""


import collections


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater_than = collections.defaultdict(lambda: -1)
        for i, n in enumerate(nums2):
            for j, m in enumerate(nums2[i+1:], start=i+1):
                if m > n:
                    greater_than[n] = m
                    break
        return [greater_than[n] for n in nums1]
