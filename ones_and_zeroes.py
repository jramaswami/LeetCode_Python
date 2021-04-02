"""
LeetCode :: April 2021 Challenge :: Ones and Zeroes
jramaswami
"""
from typing import *
from collections import Counter


def solve0(index, length_acc, zeros_acc, ones_acc, S, max_zeros, max_ones):
    """Recursive solution."""
    if index >= len(S):
        return length_acc

    # Include this string.
    local_soln = 0
    if (zeros_acc + S[index]["0"] <= max_zeros 
    and ones_acc + S[index]["1"] <= max_ones):
        local_soln = solve0(index + 1, length_acc + 1, 
                            zeros_acc + S[index]["0"], ones_acc + S[index]["1"],
                            S, max_zeros, max_ones)
    #Do not include this string.
    local_soln = max(local_soln, solve0(index + 1, length_acc, zeros_acc, 
                                        ones_acc, S, max_zeros, max_ones))

    return local_soln


class Solution:
    def findMaxForm(self, strs: List[str], max_zeros: int, max_ones: int) -> int:
        S = [Counter(s) for s in strs]
        return solve0(0, 0, 0, 0, S, max_zeros, max_ones)



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
