"""
LeetCode
2429. Minimize XOR
January 2025 Challenge
jramaswami
"""


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # How many bits to set?
        num2_bits = 0
        for b in range(32):
            mask = 1 << b
            if num2 & mask:
                num2_bits += 1

        # Try to set as many of the same bits as in num1
        # starting with the higher bits
        soln = 0
        for b in range(32, -1, -1):
            mask = 1 << b
            if num2_bits and num1 & mask:
                soln |= mask
                num2_bits -= 1
        
        # If there are any bits left over, set unset bits 
        # from bottom
        for b in range(32):
            mask = 1 << b
            if num2_bits and soln & mask == 0:
                soln |= mask
                num2_bits -= 1

        return soln
