"""
LeetCode
1444. Number of Ways of Cutting a Pizza
March 2023 Challenge
jramaswami

Thank You Larry!
"""


import functools
from typing import *


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = pow(10, 9) + 7
        soln = 0
        R = len(pizza)
        C = len(pizza[0])

        @functools.cache
        def has_apple(r1, r2, c1, c2):
            for r in range(r1, r2+1):
                for c in range(c1, c2+1):
                    if pizza[r][c] == 'A':
                        return True
            return False

        @functools.cache
        def rec(r, c, cuts_left):
            "(r, c) is upper left of remaining piece; x is number of cuts left"
            if cuts_left == 0:
                if has_apple(r, R-1, c, C-1):
                    return 1
                return 0

            result = 0
            for r_cut in range(r, R-1):
                if has_apple(r, r_cut, c, C-1) and has_apple(r_cut+1, R-1, c, C-1):
                    result += rec(r_cut+1, c, cuts_left-1)
                    result %= MOD

            for c_cut in range(c, C-1):
                if has_apple(r, R-1, c, c_cut) and has_apple(r, R-1, c_cut+1, C-1):
                    result += rec(r, c_cut+1, cuts_left-1)
                    result %= MOD
            return result % MOD

        return rec(0, 0, k-1) % MOD



def test_1():
    pizza = ["A..","AAA","..."]
    k = 3
    expected = 3
    assert Solution().ways(pizza, k) == expected


def test_2():
    pizza = ["A" * 50 for _ in range(49)]
    print(pizza)
    k = 10
    expected = 3
    assert Solution().ways(pizza, k) == expected