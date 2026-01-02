"""
LeetCode
961. N-Repeated Element in Size 2N Array
January 2026 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        freqs = collections.Counter(nums)
        for n, k in freqs.items():
            if k > 1:
                return n