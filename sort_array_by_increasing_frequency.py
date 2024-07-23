"""
LeetCode
1636. Sort Array by Increasing Frequency
July 2024 Challenge
jramaswami
"""


import collections


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freqs = [(x, -k) for k, x in collections.Counter(nums).items()]
        freqs.sort()
        soln = []
        for x, k in freqs:
            soln.extend([-k] * x)
        return soln