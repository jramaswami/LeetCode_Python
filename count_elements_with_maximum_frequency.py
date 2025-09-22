"""
LeetCode
3005. Count Elements With Maximum Frequency
September 2025 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqs = collections.Counter(nums)
        max_freq = max(freqs.values())
        return sum(f for f in freqs.values() if f == max_freq)