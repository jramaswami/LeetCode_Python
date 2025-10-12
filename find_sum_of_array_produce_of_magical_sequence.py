"""
LeetCode
3539. Find Sum of Array Product of Magical Sequences
October 2025 Challenge
jramaswami

This is probably the worst problem description I have ever read!
"""


import math
import functools


class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        MOD = pow(10, 9) + 7

        @functools.cache
        def rec(remaining, odd_needed, index, carry):
            if remaining < 0 or odd_needed < 0 or remaining + carry.bit_count() < odd_needed:
                return 0
            if remaining == 0:
                return 1 if odd_needed == carry.bit_count() else 0
            if index >= len(nums):
                return 0

            ans = 0
            for take in range(remaining + 1):
                ways = math.comb(remaining, take) * pow(nums[index], take, MOD) % MOD
                new_carry = carry + take
                ans += ways * rec(remaining - take, odd_needed - (new_carry % 2), index + 1, new_carry // 2)
                ans %= MOD
            return ans

        return rec(m, k, 0, 0) % MOD