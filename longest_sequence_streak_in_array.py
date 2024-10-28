"""
LeetCode
2501. Longest Square Streak in an Array
October 2024 Challenge
jramaswami
"""


import collections


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        prev = collections.defaultdict(int)
        for n in nums:
            x = n * n
            prev[n] = max(prev[x] + 1, prev[n])
        soln = max(prev.values())
        return -1 if soln < 2 else soln
