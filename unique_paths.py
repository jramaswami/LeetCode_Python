"""
LeetCode :: November 2021 Challenge :: 62. Unique Paths
jramaswami
"""


import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def nCk(n, k):
            return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

        m -= 1
        n -= 1
        return nCk(m + n, m)