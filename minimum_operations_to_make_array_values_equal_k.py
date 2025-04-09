"""
LeetCode
3375. Minimum Operations to Make Array Values Equal to K
April 2025 Challenge
jramaswami
"""


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums0 = list(sorted(set(nums)))
        if nums0[0] < k:
            return -1
        elif nums0[0] == k:
            return len(nums0) - 1
        return len(nums0)