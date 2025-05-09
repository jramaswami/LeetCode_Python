"""
LeetCode
3343. Count Number of Balanced Permutations
May 2025 Challenge
jramaswami

REF: https://leetcode.doocs.org/en/lc/3343/#solution-1-memoization-search-combinatorial-mathematics
"""


import collections
import functools
import math


class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = pow(10, 9) + 7
        T = sum(int(x) for x in num)
        if T % 2:
            return 0
        N = len(num)
        freqs = collections.Counter(int(x) for x in num)

        @functools.cache
        def rec(i, j, a, b):
            # i = curr digit, j = remaining odd sum, a = remaining odd, b = remaining even
            # Base Case
            if i > 9:
                return (j | a | b) == 0
            if a == 0 and j:
                return 0
            result = 0
            for l in range(min(a, freqs[i]) + 1):
                r = freqs[i] - l
                if 0 <= r <= b and l * i <= j:
                    t = (math.comb(a, l) * math.comb(b, r) * rec(i + 1, j - l * i, a - l, b - r))
                    result += t
                    result %= MOD
            return result

        return rec(0, T // 2, N // 2, (N+1) // 2) % MOD


def test_1():
    num = '123'
    assert Solution().countBalancedPermutations(num) == 2
