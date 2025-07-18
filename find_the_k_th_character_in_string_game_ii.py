"""
LeetCode
3307. Find the K-th Character in String Game II
July 2025 Challenge
jramaswami
"""


import math
from typing import List


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        def shift(c):
            x = ord(c) - ord('a')
            x = (x + 1) % 26
            return chr(x + ord('a'))

        soln = "a"
        for bit, op in zip(reversed(bin(k-1)[2:]), operations):
            if int(bit) and op:
                soln = shift(soln)
        return soln


def test_1():
    k = 5
    operations = [0,0,0]
    expected = "a"
    assert Solution().kthCharacter(k, operations) == expected


def test_2():
    k = 10
    operations = [0,1,0,1]
    expected = "b"
    assert Solution().kthCharacter(k, operations) == expected


def test_3():
    "WA"
    k = 1
    operations = [0, 1]
    expected = "a"
    assert Solution().kthCharacter(k, operations) == expected