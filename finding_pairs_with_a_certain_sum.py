"""
LeetCode
1865. Finding Pairs With a Certain Sum
July 2025 Challenge
jramaswami
"""


import collections
from typing import List


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freqs = collections.Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.freqs[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.freqs[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        result = 0
        for i, x in enumerate(self.nums1):
            y = tot - x
            result += self.freqs[y]
        return result

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)