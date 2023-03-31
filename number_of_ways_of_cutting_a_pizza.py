"""
LeetCode
1444. Number of Ways of Cutting a Pizza
March 2023 Challenge
jramaswami

Thank You Larry!
"""


from typing import *


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = pow(10, 9) + 7
        soln = 0

        mat_sum = [[0 for _ in row] for row in pizza]
        for c, _ in enumerate(pizza[0]):
            row_sum = 0
            for r, _ in enumerate(pizza):
                if pizza[r][c] == 'A':
                    row_sum += 1
                col_sum = mat_sum[r][c-1] if c > 0 else 0
                mat_sum[r][c] = col_sum + row_sum

        def get_mat_sum_value(r, c):
            if r < 0 or c < 0:
                return 0
            return mat_sum[r][c]

        def get_mat_sum(r1, c1, r2, c2):
            A = get_mat_sum_value(r2, c2)
            B = get_mat_sum_value(r1-1, c2)
            C = get_mat_sum_value(r2, c1-1)
            D = get_mat_sum_value(r1-1, c1-1)
            return A - B - C + D

        def has_apple(r1, c1, r2, c2):
            print(f'has_apple({r1}, {c1}, {r2}, {c2}) =', get_mat_sum(r1, c1, r2, c2) > 0)
            return get_mat_sum(r1, c1, r2, c2) > 0

        def rec(r1, c1, r2, c2, cuts_left):
            print(f'rec', r1, c1, r2, c2, cuts_left)
            if cuts_left == 0:
                return 1

            result = 0
            for c_cut in range(c1, c2-1):
                if has_apple(r1, c1, r2, c_cut) and has_apple(r1, c_cut+1, r2, c2):
                    result += rec(r1, c_cut+1, r2, c2, cuts_left - 1)
                    result %= MOD
            for r_cut in range(r1, r2-1):
                if has_apple(r1, c1, r_cut, c2) and has_apple(r_cut+1, c1, r2, c2):
                    result += rec(r_cut+1, c1, r2, c2, cuts_left - 1)
                    result %= MOD

            return result %MOD

        soln = rec(0, 0, len(pizza)-1, len(pizza[-1])-1, k-1)
        return soln % MOD



def test_1():
    pizza = ["A..","AAA","..."]
    k = 3
    expected = 3
    assert Solution().ways(pizza, k) == expected