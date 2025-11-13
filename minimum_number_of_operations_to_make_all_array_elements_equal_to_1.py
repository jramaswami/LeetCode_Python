"""
LeetCode
2654. Minimum Number of Operations to Make All Array Elements Equal to 1
November 2025 Challenge
jramaswami

REF: https://algo.monster/liteproblems/2654
"""


import math
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        ones = nums.count(1)
        if ones:
            return N - ones

        min_length = N + 1
        for left, _ in enumerate(nums):
            g = nums[left]
            for right, val in enumerate(nums[left+1:], start=left+1):
                g = math.gcd(g, val)
                if g == 1:
                    min_length = min(min_length, right - left + 1)
                    break

        if min_length > N:
            return -1
        return N - 1 + min_length - 1