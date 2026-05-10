"""
LeetCode
2770. Maximum Number of Jumps to Reach the Last Index
May 2026 Challenge
jramaswami
"""


import math
import collections


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        distance = [-math.inf for _ in nums]
        distance[0] = 0
        for i, _ in enumerate(nums):
            for j, _ in enumerate(nums[i+1:], start=i+1):
                if -target <= nums[j] - nums[i] <= target:
                    distance[j] = max(distance[j], 1+distance[i])
        if distance[-1] == -math.inf:
            return -1
        return distance[-1]