"""
LeetCode
2784. Check if Array is Good
May 2026 Challenge
jramaswami
"""


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        N = len(nums)
        base = list(range(1, N))
        base.append(N-1)
        nums.sort()
        return base == nums