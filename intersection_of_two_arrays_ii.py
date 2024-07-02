"""
LeetCode
350. Intersetcion of Two Arrays II
July 2024 Challenge
jramaswami
"""


import collections
import itertools


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = collections.Counter(nums1)
        counter2 = collections.Counter(nums2)
        soln = []
        for x in set(itertools.chain(nums1, nums2)):
            t = min(counter1[x], counter2[x])
            soln.extend((x for _ in range(t)))
        return soln
