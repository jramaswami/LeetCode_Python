"""
LeetCode
3289. The Two Sneaky Numbers of Digitville
October 2025 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freqs = collections.Counter(nums)
        return [n for n in freqs if freqs[n] > 1]