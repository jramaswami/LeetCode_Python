"""
LeetCode
1420. Build Array Where You Can Find The Maximum Exactly K Comparisons
October 2023 Challenge
jramaswami
"""


import functools


class Solution:
    def numOfArrays(self, array_length: int, max_value: int, max_maxes: int) -> int:
        MOD = pow(10, 9) + 7

        @functools.cache
        def rec(curr_index: int, maxes_found: int, curr_max: int) -> int:
            # Base Case
            if curr_index >= array_length:
                if maxes_found == max_maxes:
                    return 1
                return 0

            # Recursive Case
            # Can I add more maxes?
            result = 0
            if maxes_found < max_maxes:
                # Compute number of ways for each new max.
                for x in range(max(curr_max+1, 1), max_value+1):
                    result += rec(curr_index+1, maxes_found+1, x)
                    result %= MOD
            # Skip ahead without making a max.
            # I can choose any number <= curr_max.
            for x in range(1, curr_max+1):
                result += rec(curr_index+1, maxes_found, curr_max)
                result %= MOD

            return result % MOD

        return rec(0, 0, -1)


def test_1():
    n, m, k = 2, 3, 1
    expected = 6
    assert Solution().numOfArrays(n,m,k) == expected


def test_2():
    n, m, k = 5, 2, 3
    expected = 0
    assert Solution().numOfArrays(n,m,k) == expected


def test_3():
    n, m, k = 9, 1, 1
    expected = 1
    assert Solution().numOfArrays(n,m,k) == expected