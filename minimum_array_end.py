"""
LeetCode
3133. Minimum Array End
November 2024 Challenge
jramaswami
"""


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # Need to add n-1 bits
        i = 0
        j = 0
        t = n - 1
        while n > 1 and j <= 50:
            mask_x = 1 << j
            # empty bit 
            if mask_x & x == 0:
                mask_t = 1 << i
                if t & mask_t:
                    x |= mask_x
                i += 1
                n -= 1
            j += 1
        return x
