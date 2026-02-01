"""
LeetCode
3010. Divide an Array Into Subarrays With Minimum Cost I
February 2026 Challenge
jramaswami
"""


import heapq


class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        return nums[0] + sum(heapq.nsmallest(2, nums[1:]))