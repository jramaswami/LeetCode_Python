"""
Leet Code :: May 2021 Challenge :: Super Palindromes
jramaswami
"""
from typing import *


class Solution:
    def superpalindromesInRange(self, L: str, R: str) -> int:
        left, right = int(L), int(R)
        max_base = pow(10, 9)
        max_super_palindrome = right
        soln = 0
        # Odd length palindromes
        for base in range(max_base):
            s = str(base)
            p = int(s + s[-2::-1])
            psq = p * p
            if psq > max_super_palindrome:
                break
            psq_s = str(psq)
            if psq_s == psq_s[::-1] and psq >= left and psq <= right:
                soln += 1

        # Even length palindromes
        for base in range(max_base):
            s = str(base)
            p = int(s + s[::-1])
            psq = p * p
            if psq > max_super_palindrome:
                break
            psq_s = str(psq)
            if psq_s == psq_s[::-1] and psq >= left and psq <= right:
                soln += 1

        return soln


def test_1():
    left = "4"
    right = "1000"
    assert Solution().superpalindromesInRange(left,right) == 4


def test_2():
    left = "1"
    right = "2"
    assert Solution().superpalindromesInRange(left, right) == 1