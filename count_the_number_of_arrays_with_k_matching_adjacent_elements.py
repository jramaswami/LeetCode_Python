"""
LeetCode
3405. Count the Number of Arrays with K Matching Adjacent Elements
June 2025 Challenge
jramaswami

Thank You Larry!
"""


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = pow(10, 9) + 7
        return (m * pow(m-1, n-1-k, MOD) * comb(n - 1, k)) % MOD