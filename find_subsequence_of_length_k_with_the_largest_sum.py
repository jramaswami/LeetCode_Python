"""
LeetCode
2099. Find Subsequence of Length K With the Largest Sum
June 2025 Challenge
jramaswami
"""


import operator


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        A = list(sorted((-x, i) for i, x in enumerate(nums)))
        return [-x for x, i in sorted(A[:k], key=operator.itemgetter(1))]