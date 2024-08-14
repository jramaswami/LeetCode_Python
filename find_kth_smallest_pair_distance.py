"""
LeetCode
719. Find K-th Smallest Pair Distance
August 2024 Challenge
jramaswami

Thank You NeetCode.io!
"""


import math


class Solution:

    def smallestDistancePair(self, nums, k):
        nums.sort()

        def count_pairs(x):
            lte = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > x:
                    left += 1
                lte += (right - left)
            return lte

        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            x = lo + ((hi - lo) // 2)
            if count_pairs(x) >= k:
                hi = x
            else:
                lo = x + 1
        return hi