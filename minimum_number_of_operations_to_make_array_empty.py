"""
LeetCode
2870. Minimum Number of Operations to Make Array Empty
January 2024 Challenge
jramaswami
"""


import collections


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freqs = list(collections.Counter(nums).values())
        soln = 0
        for f in freqs:
            if f == 1:
                return -1
            q, r = divmod(f, 3)
            if r == 0:
                # Just get there with 3s
                soln += q
            else:
                # If r == 1 then we back out one 3 and add two 2s
                # If r == 2 then we just add a 2
                soln += (q + 1)
        return soln