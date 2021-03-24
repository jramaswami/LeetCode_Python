"""
LeetCode :: March 2021 Challenge :: Advantage Shuffle
jramaswami
"""
from typing import *


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A0 = sorted(A)
        B0 = sorted((b, i) for i, b in enumerate(B))

        discarded_B = []

        soln = [None for _ in A]

        while B0:
            while B0 and A0[-1] <= B0[-1][0]:
                discarded_B.append(B0[-1])
                B0.pop()

            if B0:
                i = B0[-1][1]
                soln[i] = A0[-1]
                B0.pop()
                A0.pop()

        for a, b in zip(A0, discarded_B):
            i = b[1]
            soln[i] = a

        return soln


def test_1():
    A = [2,7,11,15]
    B = [1,10,4,11]
    expected = [2,11,7,15]
    assert Solution().advantageCount(A, B) == expected

def test_2():
    A = [12,24,8,32]
    B = [13,25,32,11]
    expected = [24,32,8,12]
    assert Solution().advantageCount(A, B) == expected

