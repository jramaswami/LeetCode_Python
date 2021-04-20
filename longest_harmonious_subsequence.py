"""
LeetCode :: Longest Harmonious Subsequence
jramaswami
"""
from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ctr = Counter(nums)
        sorted_keys = sorted(ctr.keys())
        soln = 0
        for k1, k2 in zip(sorted_keys[:-1], sorted_keys[1:]):
            if k2 - k1 == 1:
                soln = max(soln, ctr[k1] + ctr[k2])
        return soln