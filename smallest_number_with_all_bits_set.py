"""
LeetCode
3370. Smallest Number With All Set Bits
October 2025 Challenge
jramaswami
"""


class Solution:
    def smallestNumber(self, n: int) -> int:
        x = 1
        while x < n:
            x *= 2
        y = x - 1
        return n | y