"""
LeetCode
3753. Total Waviness of Numbers in Range II
June 2026 Challenge
jramaswami

REF: https://www.youtube.com/watch?v=14LWUks2a94
"""


import functools


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        @functools.cache
        def rec(limit):
            digits = [int(x) for x in str(limit)]

            @functools.cache
            def dp(i, prev, tight, curr, trend):
                if i == len(digits): return curr
                mx = digits[i] if tight else 9
                res = 0
                for d in range(mx+1):
                    if i == 0 and d == 0:
                        continue
                    tight0 = tight and d == mx
                    curr0 = curr
                    if trend == 1 and d < prev:
                        curr0 += 1
                    elif trend == 2 and d > prev:
                        curr0 += 1
                    if d == prev or i == 0:
                        trend0 = 0
                    elif d > prev:
                        trend0 = 1
                    elif d < prev:
                        trend0 = 2
                    res += dp(i+1, d, tight0, curr0, trend0)

                return res

            return dp(0, 0, True, 0, 0)

        @functools.cache
        def solve(limit):
            total_digits = len(str(limit))
            res = 0
            for digits in range(1, total_digits):
                largest = 10**digits - 1
                res += rec(largest)
            res += rec(limit)
            return res

        soln = solve(num2) - solve(num1)
        s = str(num1)
        for i in range(1, len(s)-1):
            if s[i-1] < s[i] > s[i+1] or s[i-1] > s[i] < s[i+1]:
                soln += 1
        return soln