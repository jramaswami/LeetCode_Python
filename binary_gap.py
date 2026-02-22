"""
LeetCode
868. Binary Gap
February 2026 Challenge
jramaswami
"""


class Solution:
    def binaryGap(self, n: int) -> int:
        set_bits = []
        for bit in range(32):
            mask = 1 << bit
            if mask & n:
                set_bits.append(bit)
        if len(set_bits) >= 2:
            return max(b - a for a, b in zip(set_bits[:-1], set_bits[1:]))
        return 0
