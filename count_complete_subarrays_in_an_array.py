"""
LeetCode
2799. Count Complete Subarrays in an Array
April 2025 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        soln = 0
        total_unique_items = len(set(nums))
        for start in range(len(nums)):
            freqs = collections.Counter()
            unique_items = 0
            arr = []
            for x in nums[start:]:
                arr.append(x)
                freqs[x] += 1
                if freqs[x] == 1:
                    unique_items += 1
                if unique_items == total_unique_items:
                    soln += 1
        return soln


def test_1():
    nums = [1, 3, 1, 2, 2]
    expected = 4
    assert Solution().countCompleteSubarrays(nums) == expected