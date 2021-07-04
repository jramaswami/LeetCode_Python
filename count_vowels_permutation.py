"""
LeetCode :: July 2021 Challenge :: Count Vowels Permutation
jramaswami
"""


class Solution:
    def countVowelPermutation(self, n):
        MOD = pow(10, 9) + 7
        curr_a = curr_e = curr_i = curr_o = curr_u = 1
        next_a = next_e = next_i = next_o = next_u = 0
        for _ in range(1, n):
            # a my only be followed by e
            next_e = (next_e + curr_a) % MOD
            # e may only be followed by an a or an i
            next_a = (next_a + curr_e) % MOD
            next_i = (next_i + curr_e) % MOD
            # i may not be followed by another i
            next_a = (next_a + curr_i) % MOD
            next_e = (next_e + curr_i) % MOD
            next_o = (next_o + curr_i) % MOD
            next_u = (next_u + curr_i) % MOD
            # o may only be followed by an i or a u
            next_i = (next_i + curr_o) % MOD
            next_u = (next_u + curr_o) % MOD
            # u may only be followed by an a
            next_a = (next_a + curr_u) % MOD

            curr_a = next_a
            curr_e = next_e
            curr_i = next_i
            curr_o = next_o
            curr_u = next_u
            next_a = next_e = next_i = next_o = next_u = 0

        soln = (curr_a + curr_e) % MOD
        soln = (soln + curr_i) % MOD
        soln = (soln + curr_o) % MOD
        soln = (soln + curr_u) % MOD
        return soln


def test_1():
    assert Solution().countVowelPermutation(1) == 5


def test_2():
    assert Solution().countVowelPermutation(2) == 10


def test_3():
    assert Solution().countVowelPermutation(5) == 68
