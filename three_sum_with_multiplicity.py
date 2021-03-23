"""
LeetCode :: 3Sum With Multiplicity
jramaswami
"""
from typing import *
from collections import Counter
from math import factorial


MOD = pow(10, 9) + 7


def nCk(n, k):
    """Return n choose k."""
    return factorial(n) // (factorial(k) * factorial(n - k))


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ctr = Counter(arr)
        keys = sorted(ctr)
        soln = 0
        for i, a in enumerate(keys):
            for j, b in enumerate(keys[i:], start=i):
                c = target - (a + b)
                if c in ctr and c >= b:
                    # Cases
                    if a == b:
                        t = (nCk(ctr[a], 2) * ctr[c]) % MOD
                        soln = (soln + t) % MOD
                    elif b == c:
                        t = (ctr[a] * nCk(ctr[b], 2)) % MOD
                        soln = (soln + t) % MOD
                    elif a == b == c:
                        t = (nCk(ctr[a], 3)) % MOD
                        soln = (soln + t) % MOD
                    else:
                        t = (ctr[a] * ctr[b] * ctr[c]) % MOD
                        soln = (soln + t) % MOD
        return soln


def test_1():
    arr = [1,1,2,2,3,3,4,4,5,5]
    target = 8
    assert Solution().threeSumMulti(arr, target) == 20

def test_2():
    arr = [1,1,2,2,2,2]
    target = 5
    assert Solution().threeSumMulti(arr, target) == 12

def test_3():
    arr = [0,0,0]
    target = 0
    assert Solution().threeSumMulti(arr, target) == 1
