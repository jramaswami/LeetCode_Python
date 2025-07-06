"""
LeetCode
1865. Finding Pairs With a Certain Sum
July 2025 Challenge
jramaswami
"""


from typing import List


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        self.nums2[index] += val

    def count(self, tot: int) -> int:
        result = 0
        for i, x in enumerate(self.nums1):
            for j, y in enumerate(self.nums2):
                if x + y == tot:
                    result += 1
        return result

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)