"""
LeetCode
989. Add to Array-Form of Integer
February 2023 Challenge
jramaswami
"""


import itertools
from typing import *


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        addend = [int(i) for i in str(k)]
        soln = []
        carry = 0
        for a, b in itertools.zip_longest(reversed(num), reversed(addend), fillvalue=0):
            p = a + b + carry
            carry, q = divmod(p, 10)
            soln.append(q)
        if carry:
            soln.append(carry)
        return soln[::-1]


def test_1():
    num = [1,2,0,0]
    k = 34
    expected = [1,2,3,4]
    assert Solution().addToArrayForm(num, k) == expected


def test_2():
    num = [2,7,4]
    k = 181
    expected = [4,5,5]
    assert Solution().addToArrayForm(num, k) == expected


def test_3():
    num = [2,1,5]
    k = 806
    expected = [1,0,2,1]
    assert Solution().addToArrayForm(num, k) == expected