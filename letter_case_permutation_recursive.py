"""
LeetCode :: Letter Case Permutation
Recursive solution
jramaswami
"""
from typing import *


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def solve0(index, S0, acc):
            """Recursively produce every possible capitilzation."""
            if index >= len(S0):
                acc.append("".join(S0))
            else:
                # Only recurse twice if S0 is a letter.
                if S0[index].isalpha():
                    # uppercase
                    S0[index] = S0[index].upper()
                    solve0(index + 1, S0, acc)
                    S0[index] = S0[index].lower()
                    solve0(index + 1, S0, acc)
                else:
                    solve0(index + 1, S0, acc)

        acc = []
        solve0(0, [c for c in S], acc)
        return acc


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
