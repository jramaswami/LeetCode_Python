"""
LeetCode
2566. Maximum Difference by Remapping a Digit
June 2025 Challenge
jramaswami
"""


class Solution:
    def minMaxDifference(self, num: int) -> int:
        S = str(num)
        # For minimum, replace the first value with zero
        multiplier = pow(10, len(S) - 1)
        min_value = 0
        for digit in S:
            if digit != S[0]:
                min_value += (multiplier * int(digit))
            multiplier //= 10

        # For maximum, replace first non-nine digit with 9
        multiplier = pow(10, len(S) - 1)
        max_value = 0
        replacing = None
        for digit in S:
            if digit == '9':
                max_value += (multiplier * 9)
            elif replacing:
                if digit == replacing:
                    max_value += (multiplier * 9)
                else:
                    max_value += (multiplier * int(digit))
            else:
                replacing = digit
                max_value += (multiplier * 9)
            multiplier //= 10

        return max_value - min_value