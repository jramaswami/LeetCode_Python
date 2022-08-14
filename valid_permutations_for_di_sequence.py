"""
LeetCode :: 903. Valid Permutations for DI Sequence
jramaswami
"""


import functools



class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = pow(10, 9) + 7

        @functools.cache
        def solve(last_num, avail_nums):
            if not avail_nums:
                return 1
            i = len(s) - len(avail_nums)
            result = 0
            if s[i] == 'D':
                for k in avail_nums:
                    if k < last_num:
                        result = (
                            result +
                            solve(k, avail_nums - frozenset([k]))
                        ) % MOD
            else:
                for k in avail_nums:
                    if k > last_num:
                        result = (
                            result +
                            solve(k, avail_nums - frozenset([k]))
                        ) % MOD
            return result % MOD

        soln = 0
        avail_nums = frozenset(range(len(s)+1))
        for k in avail_nums:
            soln = (soln + solve(k, avail_nums - frozenset([k]))) % MOD
        return soln % MOD


def test_1():
    s = "DID"
    expected = 5
    assert Solution().numPermsDISequence(s) == expected