"""
LeetCode
762. Prime Number of Set Bits in Binary Representation
February 2026 Challenge
jramaswami
"""


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        PRIMES = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
        soln = 0
        for n in range(left, right+1):
            if n.bit_count() in PRIMES:
                soln += 1
        return soln
