"""
LeetCode
2537. Count the Number of Good Subarrays
April 2025 Challenge
jramaswami
"""


import collections
import math


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        def pair_count(n):
            return (n * (n-1)) // 2

        soln = 0
        for left, _ in enumerate(nums):
            freqs = collections.Counter()
            curr_pairs = 0
            for right, x in enumerate(nums[left:], start=left):
                # Add x to the list of items
                if x in freqs:
                    curr_pairs -= pair_count(freqs[x])
                freqs[x] += 1
                curr_pairs += pair_count(freqs[x])
                if curr_pairs >= k:
                    soln += 1
        return soln