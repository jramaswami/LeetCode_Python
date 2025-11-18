"""
LeetCode
717. 1-bit and 2-bit Characters
November 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        carry = False
        for n in bits[:-1]:
            if n == 0:
                carry = False
            elif n == 1:
                if carry:
                    carry = False
                else:
                    carry = True
        return not carry