"""
LeetCode :: Letter Case Permutation
jramaswami
"""
from typing import *
from itertools import combinations


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        # Set of solutions
        solns = set()
        # For each bitmask in the range [0, 1 << len(S)) all the 1s are
        # uppercase and all the 0s are lowercase.  This will get every 
        # possibility and we use a set to reduce duplicates.
        # O(2^N * N) but it is such a small N this is fast enough.
        for mask in range(1 << len(S)):
            S0 = list(S)
            for bit in range(len(S)):
                if (1 << bit) & mask:
                    S0[bit] = S0[bit].upper()
                else:
                    S0[bit] = S0[bit].lower()
            solns.add("".join(S0))
        return list(solns)


def test_1():
    S = "a1b2"
    T = sorted(["a1b2","a1B2","A1b2","A1B2"])
    assert sorted(Solution().letterCasePermutation(S)) == T


def test_2():
    S = "3z4"
    T = sorted(["3z4","3Z4"])
    assert sorted(Solution().letterCasePermutation(S)) == T


def test_3():
    S = "12345"
    T = sorted(["12345"])
    assert sorted(Solution().letterCasePermutation(S)) == T


def test_4():
    S = "0"
    T = sorted(["0"])
    assert sorted(Solution().letterCasePermutation(S)) == T


def test_5():
    S = "C"
    T = sorted(["c","C"])
    assert sorted(Solution().letterCasePermutation(S)) == T
