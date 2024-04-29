"""
LeetCode
2997. Minimum Number of Operations to Make Array XOR Equal to K
April 2024 Challenge
jramaswami
"""


import functools
import operator


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        x = functools.reduce(operator.xor, nums, 0)
        y = x ^ k
        return y.bit_count()