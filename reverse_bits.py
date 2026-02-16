"""
LeetCode
190. Reverse Bits
February 2026 Challenge
jramaswami
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        soln = 0
        for i in range(32):
            mask = 1 << i
            bit = n & mask
            soln = soln << 1
            if bit:
                soln += 1
        return soln