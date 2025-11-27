"""
LeetCode
3381. Maximum Subarray Sum With Length Divisible by K
November 2025 Challenge
jramaswami
"""


import math
from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        cache = {}
        cache[0] = 0
        curr_sum = 0
        soln = -math.inf
        for i, n in enumerate(nums, start=1):
            curr_sum += n
            j = i % k
            if j in cache:
                soln = max(soln, curr_sum - cache[j])
            if j not in cache or cache[j] > curr_sum:
                cache[j] = curr_sum
        return soln