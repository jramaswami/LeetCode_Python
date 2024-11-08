"""
LeetCode
1829. Maximum XOR for Each Query
November 2024 Challenge
jramaswami
"""


import functools
import operator


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        x = functools.reduce(operator.xor, nums)
        soln = []
        for i in range(len(nums)-1, -1, -1):
            y = 0
            for b in range(maximumBit):
                mask = 1 << b
                if x & mask == 0:
                    y |= mask
            soln.append(y)
            x ^= nums[i]
        return soln
