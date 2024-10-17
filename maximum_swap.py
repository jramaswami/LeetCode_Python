"""
LeetCode
670. Maximum Swap
October 2024 Challenge
jramaswami
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert into a list of digits
        digits = [int(t) for t in str(num)]
        digits = digits[::-1]

        curr_max = -1
        max_posn = -1
        swap = None

        for i, n in enumerate(digits):
            if n > curr_max:
                curr_max = n
                max_posn = i
            if n < curr_max and max_posn < i:
                swap = (i, max_posn)
        
        if swap:
            i, j = swap
            digits[i], digits[j] = digits[j], digits[i]
        
        digits = digits[::-1]
        return int(''.join(str(t) for t in digits))
