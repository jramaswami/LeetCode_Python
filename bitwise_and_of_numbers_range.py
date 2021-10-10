"""
LeetCode :: October 2021 Challenge :: 201. Bitwise AND of Numbers Range
jramaswami
"""


class Solution:
    def rangeBitwiseAnd(self, left, right):
        soln = 0
        # Scan from MSB -> LSB
        for bit in range(32, -1, -1):
            mask = 1 << bit

            left_set = left & mask
            right_set = right & mask

            # If both are set then set the bit in the soln.
            if left_set and right_set:
                soln |= mask
                continue

            # If both are not set it is ok.
            if not left_set and not right_set:
                continue

            # If one is and the other is not then stop.
            break

        return soln
