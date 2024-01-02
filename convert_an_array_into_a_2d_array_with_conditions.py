"""
LeetCode
2610. Convert an Array Into a 2D Array With Conditions
January 2024 Challenge
jramaswami
"""


import collections


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freqs = collections.Counter(nums)
        soln = [[] for _ in range(max(freqs.values()))]
        for f in freqs:
            for i in range(freqs[f]):
                soln[i].append(f)
        return soln