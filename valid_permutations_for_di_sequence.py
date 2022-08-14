"""
LeetCode :: 903. Valid Permutations for DI Sequence
jramaswami

Thank You Larry!
"""


import functools


class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = pow(10, 9) + 7

        @functools.cache
        def solve(i, last_num):
            if i >= len(s):
                return 1

            nums_left = len(s) - i
            result = 0
            if s[i] == 'D':
                for k in range(last_num):
                    result = (result + solve(i+1, k)) % MOD
            else:
                for k in range(last_num, nums_left):
                    result = (result + solve(i+1, k)) % MOD
            return result % MOD

        soln = 0
        for k in range(len(s)+1):
            soln = (soln + solve(0, k)) % MOD
        return soln % MOD


def test_1():
    s = "DID"
    expected = 5
    assert Solution().numPermsDISequence(s) == expected


def test_2():
    "MLE"
    s = "IDDDIIDIIIIIIIIDIDID"
    expected = 853197538
    assert Solution().numPermsDISequence(s) == expected