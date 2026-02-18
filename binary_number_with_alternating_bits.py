"""
LeetCode
693. Binary Number with Alternating Bits
February 2026 Challenge
jramaswami
"""


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        max_bit = 0
        for b in range(32):
            mask = 1 << b
            if n & mask:
                max_bit = b

        if b < 2:
            return True

        for b in range(max_bit):
            mask1 = 1 << b
            mask2 = 1 << (b+1)
            bit1 = (mask1 & n) > 0
            bit2 = (mask2 & n) > 0
            if bit1 == bit2:
                return False
        return True