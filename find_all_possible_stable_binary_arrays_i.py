"""
LeetCode
3129. Find All Possible Stable Binary Arrays I
March 2026 Challenge
jramaswami

Thank You Larry!
"""


import functools


class Solution:
    def numberOfStableArrays(self, count_zero: int, count_one: int, limit: int) -> int:
        N = count_zero + count_one
        MOD = pow(10, 9) + 7
        soln = 0

        @functools.cache
        def rec(zeros_left, ones_left, last_used):
            # Base case
            if zeros_left == 0 and ones_left == 0:
                return 1

            count = 0

            # Use zero
            if last_used != 0:
                max_zeros = min(zeros_left, limit)
                for used_zeros in range(1, max_zeros+1):
                    count += rec(zeros_left - used_zeros, ones_left, 0)
                    count %= MOD

            # Use one
            if last_used != 1:
                max_ones = min(ones_left, limit)
                for used_ones in range(1, max_ones+1):
                    count += rec(zeros_left, ones_left - used_ones, 1)
                    count %= MOD

            return count % MOD

        soln = rec(count_zero, count_one, -1)
        return soln % MOD