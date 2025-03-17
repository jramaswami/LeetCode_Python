"""
LeetCode
2206. Divide Array Into Equal Pairs
March 2025 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freqs = collections.Counter(nums)
        return all(k % 2 == 0 for k in freqs.values())