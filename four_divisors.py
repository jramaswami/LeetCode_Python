"""
LeetCode
1390. Four Divisors
January 2026 Challenge
jramaswami
"""


from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def divisors(n):
            q, s, t = 1, 0, 0
            while q * q <= n:
                p, r = divmod(n, q)
                if r == 0:
                    if p == q:
                        t += 1
                        s += q
                    else:
                        t += 2
                        s += q
                        s += p
                q += 1
            if t == 4:
                return s
            return 0

        return sum(divisors(n) for n in nums)