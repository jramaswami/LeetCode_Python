"""
LeetCode
2683. Neighboring Bitwise XOR
January 2025 Challenge
jramaswami
"""


import functools
import operator


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return functools.reduce(operator.xor, derived) == 0
