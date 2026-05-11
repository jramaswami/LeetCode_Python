"""
LeetCode
2553. Separate the Digits in an Array
May 2026 Challenge
jramaswami
"""


import itertools


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return list(itertools.chain(*([int(c) for c in str(n)] for n in nums)))