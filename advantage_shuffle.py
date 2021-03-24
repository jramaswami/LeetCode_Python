"""
LeetCode :: March 2021 Challenge :: Advantage Shuffle
jramaswami
"""
from typing import *


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A0 = sorted(A, reverse=True)
        B0 = sorted([(b, i) for i, b in enumerate(B)], reverse=True)
        soln = [None for _ in A]
        left = 0
        right = len(A0) - 1
        for b, i in B0:
            if A0[left] > b:
                soln[i] = A0[left]
                left += 1
            else:
                soln[i] = A0[right]
                right -= 1
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

