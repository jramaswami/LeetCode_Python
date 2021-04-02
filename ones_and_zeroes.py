"""
LeetCode :: April 2021 Challenge :: Ones and Zeroes
jramaswami
"""
from typing import *
from collections import Counter, defaultdict

class Solution:
    def findMaxForm(self, strs: List[str], max_zeros: int, max_ones: int) -> int:
        curr_dp = defaultdict(int)
        next_dp = defaultdict(int)

        for s in strs:
            ctr = Counter(s)
            z_ = ctr["0"]
            o_ = ctr["1"]
            # You can always go from (0, 0).
            if z_ <= max_zeros and o_ <= max_ones:
                next_dp[(z_, o_)] = max(next_dp[(z_, o_)], 1)
            for (z, o) in curr_dp:
                next_key = (z + z_, o + o_)
                curr_key = (z, o)
                # You can skip this one.
                next_dp[curr_key] = max(next_dp[curr_key], curr_dp[curr_key])
                # Or include it.
                if z + z_ <= max_zeros and o + o_ <= max_ones:
                    next_dp[next_key] = max(next_dp[next_key], curr_dp[curr_key] + 1)

            curr_dp, next_dp = next_dp, defaultdict(int)

        return (max(curr_dp.values()) if curr_dp.values() else 0)


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
