"""
LeetCode :: May 2022 Challenge :: Ones and Zeroes
jramaswami
"""


import collections


class Solution:
    def findMaxForm(self, strs, max_zeros, max_ones):
        curr_dp = collections.defaultdict(int)
        next_dp = collections.defaultdict(int)
        curr_dp[(0, 0)] = 0
        soln = 0
        for s in strs:
            ones = s.count('1')
            zeros = len(s) - ones
            for prev_key, prev_val in curr_dp.items():
                # Without current s
                next_dp[prev_key] = max(next_dp[prev_key], prev_val)
                # With current s
                ones0, zeros0 = prev_key
                if ones0 + ones <= max_ones and zeros0 + zeros <= max_zeros:
                    next_key = (ones0 + ones, zeros0 + zeros)
                    next_dp[next_key] = max(next_dp[next_key], prev_val + 1)
                    soln = max(soln, prev_val + 1)
            curr_dp, next_dp = next_dp, collections.defaultdict(int)

        return soln


def test_1():
    strs = ["10","0001","111001","1","0"]
    m = 5
    n = 3
    assert Solution().findMaxForm(strs, m, n) == 4


def test_2():
    strs = ["10","0","1"]
    m = 1
    n = 1
    assert Solution().findMaxForm(strs, m, n) == 2


def test_3():
    """TLE"""
    strs = ["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"]
    m = 9
    n = 80
    assert Solution().findMaxForm(strs, m, n) == 17


def test_4():
    """RTE"""
    strs = ["00","000"]
    m = 1
    n = 10
    assert Solution().findMaxForm(strs, m, n) == 0
