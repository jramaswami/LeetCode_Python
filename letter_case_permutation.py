"""
LeetCode :: Letter Case Permutation
jramaswami
"""
from typing import *
from itertools import combinations


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        solns = []
        # Get the indices of the characters in S
        letter_indices = [i for i, c in enumerate(S) if c.isalpha()]
        # For each combo of indices in the powerset of the indices of the
        # letters, capitalize the letters at the indicies.
        for cap_count in range(len(letter_indices)+1):
            for combo in combinations(letter_indices, cap_count):
                S0 = [c for c in S]
                for i in combo:
                    S0[i] = S0[i].upper()
                solns.append("".join(S0))
        return solns


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
