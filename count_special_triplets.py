"""
LeetCode
3583. Count Special Triplets
Decmber 2025 Challenge
jramaswami

REF: https://algo.monster/liteproblems/3583
"""


import collections
from typing import List


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = pow(10, 9) + 7
        left = collections.Counter()
        right = collections.Counter(nums)
        result = 0
        for n in nums:
            right[n] -=1
            dv = n * 2
            tc = (left[dv] * right[dv]) % MOD
            result += tc
            result %= MOD
            left[n] += 1
        return result % MOD